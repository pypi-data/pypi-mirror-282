import os
import cv2
import uuid
import time
import json
import pyotp
import numpy
import ctypes
import random
import tkinter
import helpers
import yagmail
import win32ui
import datetime
import requests
import win32api
import win32con
import win32gui
import keyboard
import threading
import pyautogui
import win32event
import win32process
from selenium import webdriver
from webdav4.client import Client
from selenium.webdriver import Keys
from winerror import ERROR_ALREADY_EXISTS
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class 鼠标操作:
    def __init__(self, 窗口句柄):
        '''
        参数:
        窗口句柄 - 整数，表示要操作的窗口的句柄。

        示例:
        hwnd = 12345  # 这里假设为有效的窗口句柄，实际应根据情况获取
        mouse_operations = 鼠标操作(hwnd)
        '''
        self.窗口句柄 = 窗口句柄

    def 后台激活点击(self, x, y):
        """
        参数:
        x (int): 点击位置的横坐标。
        y (int): 点击位置的纵坐标。

        示例:
        hwnd = 12345  # 这里假设为有效的窗口句柄，实际应根据情况获取
        # 模拟点击 (100, 200) 坐标
        鼠标操作(hwnd).后台激活点击(100, 200)
        """
        tmp = win32api.MAKELONG(x, y)
        # 激活窗口
        win32gui.SendMessage(self.窗口句柄, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        # 发送鼠标按下和弹起消息
        win32gui.SendMessage(self.窗口句柄, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32gui.SendMessage(self.窗口句柄, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

    def 后台直接点击(self, x, y):
        """
        参数:
        x (int): 点击位置的横坐标。
        y (int): 点击位置的纵坐标。

        示例:
        hwnd = 12345  # 这里假设为有效的窗口句柄，实际应根据情况获取
        # 模拟点击 (100, 200) 坐标
        鼠标操作(hwnd).后台直接点击(100, 200)
        """
        tmp = win32api.MAKELONG(x, y)
        # 发送鼠标按下和弹起消息
        win32api.SendMessage(self.窗口句柄, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32api.SendMessage(self.窗口句柄, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)


class 找色操作:
    @staticmethod
    def 获取窗口截图(窗口句柄):
        """
        参数:
        窗口句柄 (int): 目标窗口的句柄。

        返回:
        numpy.ndarray: 包含截图像素数据的三维数组，形状为 (高度, 宽度, 3)。

        示例:
        # 假设 hwnd 为有效的窗口句柄
        hwnd = 12345
        截图 = 获取窗口截图(hwnd)
        """
        窗口设备上下文 = win32gui.GetWindowDC(窗口句柄)
        源设备上下文 = win32ui.CreateDCFromHandle(窗口设备上下文)
        内存设备上下文 = 源设备上下文.CreateCompatibleDC()

        # 获取窗口尺寸
        左, 上, 右, 下 = win32gui.GetClientRect(窗口句柄)
        宽度 = 右 - 左
        高度 = 下 - 上

        # 创建位图对象
        位图 = win32ui.CreateBitmap()
        位图.CreateCompatibleBitmap(源设备上下文, 宽度, 高度)
        内存设备上下文.SelectObject(位图)

        # 截屏到位图
        内存设备上下文.BitBlt((0, 0), (宽度, 高度), 源设备上下文, (0, 0), win32con.SRCCOPY)

        # 将位图保存为numpy数组
        位图像素数据 = 位图.GetBitmapBits(True)
        图像 = numpy.frombuffer(位图像素数据, dtype='uint8')
        图像.shape = (高度, 宽度, 4)

        # 释放内存
        源设备上下文.DeleteDC()
        内存设备上下文.DeleteDC()
        win32gui.ReleaseDC(窗口句柄, 窗口设备上下文)
        win32gui.DeleteObject(位图.GetHandle())

        # 转换为BGR格式
        图像 = cv2.cvtColor(图像, cv2.COLOR_BGRA2BGR)
        return 图像

    @staticmethod
    def 解析颜色偏移字符串(颜色偏移字符串):
        """
        解析颜色偏移字符串为偏移列表。

        参数:
        - 颜色偏移字符串 (str): 包含多个颜色偏移项的字符串，每个偏移项格式为"x偏移|y偏移|颜色"，
                            多个偏移项之间用逗号分隔。

        返回值:
        - list: 包含解析后的颜色偏移信息的列表，每个偏移信息由三部分组成：x偏移量、y偏移量和颜色值。
                颜色值以列表形式返回，包含BGR格式的整数列表，例如 [B, G, R]。

        示例:
        - 解析颜色偏移字符串("10|20|FF0000,5|-5|00FF00")
            [(10, 20, [0, 0, 255]), (5, -5, [0, 255, 0])]

        注意:
        - 颜色偏移字符串中的颜色值应为6位十六进制格式，例如 "FF0000" 表示红色。
        - 返回的颜色值列表中，颜色的顺序为BGR格式，即 [Blue, Green, Red]。
        """
        颜色偏移列表 = []
        偏移项 = 颜色偏移字符串.split(',')
        for 项 in 偏移项:
            x偏移, y偏移, 颜色 = 项.split('|')
            颜色_bgr = [int(颜色[i:i + 2], 16) for i in (4, 2, 0)]
            颜色偏移列表.append((int(x偏移), int(y偏移), 颜色_bgr))
        return 颜色偏移列表

    @staticmethod
    def 检查颜色匹配(起始颜色, x坐标, y坐标, 颜色偏移, 截图=None):
        """
        参数:
        - 起始颜色 (str): 起始颜色的十六进制表示，例如 "FF0000" 表示红色。
        - x坐标 (int): 检查像素的横坐标。
        - y坐标 (int): 检查像素的纵坐标。
        - 颜色偏移 (list): 包含颜色偏移信息的列表，每个偏移信息由三部分组成：x偏移量、y偏移量和目标颜色的BGR列表。
        - 截图 (numpy.ndarray, optional): 包含图像数据的数组，默认为 None。如果提供了截图，将在截图上进行颜色匹配检查。

        返回值:
        - bool: 如果指定位置和偏移位置上的颜色与给定的起始颜色和目标颜色匹配，则返回 True；否则返回 False。

        示例:
        起始颜色 = "FF0000"  # 红色
        x坐标 = 100
        y坐标 = 50
        颜色偏移 = [(10, 20, [0, 0, 255]), (5, -5, [0, 255, 0])]
        检查颜色匹配(起始颜色, x坐标, y坐标, 颜色偏移, 截图)
        """
        起始颜色_bgr = [int(起始颜色[i:i + 2], 16) for i in (4, 2, 0)]
        像素颜色 = 截图[y坐标, x坐标]

        if not numpy.all(像素颜色 == 起始颜色_bgr):
            return False

        for x偏移, y偏移, 目标颜色 in 颜色偏移:
            检查_x = x坐标 + x偏移
            检查_y = y坐标 + y偏移
            if 检查_x < 0 or 检查_x >= 截图.shape[1] or 检查_y < 0 or 检查_y >= 截图.shape[0]:
                continue

            像素颜色 = 截图[检查_y, 检查_x]
            if not numpy.all(像素颜色 == 目标颜色):
                return False
        return True

    @staticmethod
    def 查找特定坐标的匹配(颜色信息, 窗口句柄=None):
        """
        参数:
        - 颜色信息 (tuple): 包含颜色匹配所需的信息的元组，具体为 (x坐标, y坐标, 起始颜色, 颜色偏移字符串)。
          - x坐标 (int): 待检查颜色的横坐标。
          - y坐标 (int): 待检查颜色的纵坐标。
          - 起始颜色 (str): 起始颜色的十六进制表示，例如 "FF0000" 表示红色。
          - 颜色偏移字符串 (str): 描述颜色偏移信息的字符串，需要通过特定函数解析为颜色偏移列表。
        - 窗口句柄 (object, optional): 指定窗口的句柄，如果为 None，则在整个屏幕中查找。

        返回值:
        - bool: 如果指定位置和偏移位置上的颜色与给定的起始颜色和目标颜色匹配，则返回 True；否则返回 False。

        示例:
        颜色信息 = (100, 50, "FF0000", "[(10, 20, [0, 0, 255]), (5, -5, [0, 255, 0])]")  # 示例数据
        窗口句柄 = None  # 或者指定窗口句柄对象
        查找特定坐标的匹配(颜色信息, 窗口句柄)
        """
        x坐标, y坐标, 起始颜色, 颜色偏移字符串 = 颜色信息
        颜色偏移 = 找色操作.解析颜色偏移字符串(颜色偏移字符串)

        if 窗口句柄:
            截图 = 找色操作.获取窗口截图(窗口句柄)
        else:
            截图 = pyautogui.screenshot()
            截图 = cv2.cvtColor(numpy.array(截图), cv2.COLOR_RGB2BGR)
        return 找色操作.检查颜色匹配(起始颜色, x坐标, y坐标, 颜色偏移, 截图)
        # 匹配结果 = 找色操作.检查颜色匹配(起始颜色, x坐标, y坐标, 颜色偏移, 截图)
        # if 匹配结果:
        #     鼠标操作.设置匹配位置(x坐标, y坐标)
        #
        # return 匹配结果


class 窗口操作:
    def __init__(self):
        pass

    def 激活窗口(self, 句柄):
        """
        参数:
        句柄 (object): 指定要激活的窗口的句柄对象。

        返回值:
        无返回值。直接将指定窗口置于前台并激活。

        示例:
        激活窗口(窗口句柄)
        """
        try:
            # 使窗口前置并激活
            win32gui.SetForegroundWindow(句柄)
            print(f"窗口 {句柄} 已激活")
        except Exception as e:
            print(f"激活窗口时发生错误: {e}")

    def 获取窗口句柄(self, 标题=None, 类名=None, 进程=None, 坐标=False):
        """
        参数:
        标题 (str): 要匹配的窗口标题。如果提供，则返回第一个匹配的窗口句柄。
        类名 (str): 要匹配的窗口类名。如果提供，则返回第一个匹配的窗口句柄。
        进程 (str): 要匹配的窗口所属进程的执行文件名。如果提供，则返回第一个匹配的窗口句柄。
        坐标 (bool): 是否根据当前鼠标位置获取窗口句柄。如果为 True，则返回当前鼠标位置下的窗口句柄。

        返回值:
        object: 符合条件的窗口句柄。如果找不到匹配的窗口，返回 None。

        示例:
        获取窗口句柄(标题="记事本")
        获取窗口句柄(类名="Notepad")
        获取窗口句柄(进程="notepad.exe")
        获取窗口句柄(坐标=True)
        """
        if 坐标:
            time.sleep(3)
            point = win32api.GetCursorPos()
            窗口句柄 = win32gui.WindowFromPoint(point)
            return 窗口句柄

        句柄字典 = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), 句柄字典)

        for 句柄 in 句柄字典:
            if 标题 and 标题.strip() in win32gui.GetWindowText(句柄).strip():
                return 句柄
            if 类名 and 类名 == win32gui.GetClassName(句柄):
                return 句柄
            if 进程:
                进程id = win32process.GetWindowThreadProcessId(句柄)
                进程句柄 = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, 进程id[1])
                if 进程句柄:
                    执行文件 = win32process.GetModuleFileNameEx(进程句柄, 0)
                    if 执行文件.endswith(进程):
                        return 句柄
        return None


class 网页操作:
    def __init__(self, driver=None):
        """
        参数:
        driver: WebDriver 对象，用于控制浏览器操作的驱动程序。如果为 None，则调用创建驱动程序方法创建一个新的驱动程序。

        示例:
        obj = MyClass()  # 创建一个 MyClass 实例，使用默认的 driver 参数值为 None
        obj.driver  # 返回创建的驱动程序对象或者 None（如果创建失败）
        """
        self.driver = driver
        if self.driver is None:
            self.创建驱动程序()

    def 获取定位器(self, by):
        """
        参数:
        by (str): 定位策略的字符串表示。支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。

        返回值:
        object: 返回对应的 WebDriver 定位器对象，如果传入的定位策略不支持或未定义，则返回 None。

        示例:
        obj = MyClass()
        obj.获取定位器('ID')  # 返回 By.ID
        obj.获取定位器('CSS_SELECTOR')  # 返回 By.CSS_SELECTOR
        obj.获取定位器('XYZ')  # 返回 None，因为'XYZ'不是支持的定位策略
        """
        定位器 = {
            'ID': By.ID,
            'NAME': By.NAME,
            'CLASS_NAME': By.CLASS_NAME,
            'TAG_NAME': By.TAG_NAME,
            'LINK_TEXT': By.LINK_TEXT,
            'PARTIAL_LINK_TEXT': By.PARTIAL_LINK_TEXT,
            'CSS_SELECTOR': By.CSS_SELECTOR,
            'xp': By.XPATH
        }
        return 定位器.get(by, None)

    def 查找单个元素(self, by, 元素):
        """
        参数:
        by (str): 定位策略的字符串表示。应为大写形式，支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。
        元素 (str): 要查找的元素的定位信息，如 ID 名称、类名、标签名、链接文本、部分链接文本、CSS 选择器或 XPath 表达式。

        返回值:
        object: 返回找到的 WebElement 对象，如果找不到元素则抛出异常并返回 None。

        示例:
        obj = MyClass()
        obj.查找单个元素('ID', 'my_element_id')  # 返回 WebElement 对象
        obj.查找单个元素('CSS_SELECTOR', '.my_class')  # 返回 WebElement 对象
        obj.查找单个元素('XYZ', 'element_xyz')  # 如果找不到元素，则抛出异常并返回 None
        """
        try:
            return self.driver.find_element(self.获取定位器(by), 元素)
        except:
            pass

    def 查找多个元素(self, by, 元素):
        """
        参数:
        by (str): 定位策略的字符串表示。应为大写形式，支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。
        元素 (str): 要查找的元素的定位信息，如 ID 名称、类名、标签名、链接文本、部分链接文本、CSS 选择器或 XPath 表达式。

        返回值:
        list: 返回一个 WebElement 对象的列表，如果找不到元素则返回空列表。

        示例:
        obj = MyClass()
        obj.查找多个元素('TAG_NAME', 'a')  # 返回包含多个 WebElement 对象的列表
        obj.查找多个元素('CSS_SELECTOR', '.my_class')  # 返回包含多个 WebElement 对象的列表
        obj.查找多个元素('XYZ', 'element_xyz')  # 如果找不到元素，则抛出异常并返回空列表
        """
        try:
            return self.driver.find_elements(self.获取定位器(by), 元素)
        except Exception as e:
            raise Exception(f'查找多个元素时出错: {str(e)}')

    def 获取元素文本(self, by, 元素):
        """
        参数:
        - by (str): 定位策略的字符串表示。应为大写形式，支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。
        - 元素 (str): 要获取文本内容的元素的定位信息，如 ID 名称、类名、标签名、链接文本、部分链接文本、CSS 选择器或 XPath 表达式。

        返回值:
        - str: 返回指定元素的文本内容。

        示例:
        obj = MyClass()
        obj.获取元素文本('CSS_SELECTOR', '.my_class')  # 返回指定元素的文本内容
        obj.获取元素文本('ID', 'element_id')  # 返回指定元素的文本内容
        obj.获取元素文本('XYZ', 'element_xyz')  # 如果找不到元素或获取文本内容失败，则抛出异常
        """
        try:
            return self.查找单个元素(by, 元素).text
        except Exception as e:
            raise Exception(f'查找单个元素时出错: {str(e)}')

    def 获取元素属性(self, by, 元素, 属性):
        """
        参数:
        - by (str): 定位策略的字符串表示。应为大写形式，支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。
        - 元素 (str): 要获取属性值的元素的定位信息，如 ID 名称、类名、标签名、链接文本、部分链接文本、CSS 选择器或 XPath 表达式。
        - 属性 (str): 要获取的属性名称。

        返回值:
        - str: 返回指定元素的属性值。

        示例:
        obj = MyClass()
        obj.获取元素属性('CSS_SELECTOR', '.my_class', 'href')  # 返回指定元素的 href 属性值
        obj.获取元素属性('ID', 'element_id', 'value')  # 返回指定元素的 value 属性值
        obj.获取元素属性('XYZ', 'element_xyz', 'attribute_name')  # 如果找不到元素或获取属性值失败，则抛出异常
        """
        try:
            return self.查找单个元素(by, 元素).get_attribute(属性)
        except Exception as e:
            raise Exception(f'获取元素属性时出错: {str(e)}')

    def 设置隐式等待(self, 等待时间):
        """
        参数:
        等待时间 (int): 等待的时间长度，以秒为单位。

        示例:
        obj = MyClass()
        obj.设置隐式等待(10)  # 设置隐式等待时间为 10 秒
        """
        try:
            self.driver.implicitly_wait(等待时间)
        except Exception as e:
            raise Exception(f'设置隐式等待时出错: {str(e)}')

    def 等待元素可见(self, 超时时间, by, 元素):
        """
        参数:
        超时时间 (int): 等待的最长时间，以秒为单位。
        by (str): 定位策略的字符串表示，应为大写形式，支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。
        元素 (str): 要等待可见的元素的定位信息，如 ID 名称、类名、标签名、链接文本、部分链接文本、CSS 选择器或 XPath 表达式。

        返回值:
        bool: 如果元素在超时时间内变为可见，则返回 True；否则返回 False。

        示例:
        obj = MyClass()
        obj.等待元素可见(10, 'CSS_SELECTOR', '.my_class')  # 等待直到类名为 .my_class 的元素可见，超时时间为 10 秒
        """
        try:
            WebDriverWait(self.driver, 超时时间).until(
                expected_conditions.visibility_of_element_located((self.获取定位器(by), 元素)))
            return True
        except:
            return False

    def 等待元素出现(self, 超时时间, by, 元素):
        """
        等待直到元素出现在DOM中。

        参数:
        - 超时时间 (int): 等待的最长时间，以秒为单位。
        - by (str): 定位策略的字符串表示，应为大写形式，支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。
        - 元素 (str): 要等待出现的元素的定位信息，如 ID 名称、类名、标签名、链接文本、部分链接文本、CSS 选择器或 XPath 表达式。

        返回值:
        - bool: 如果元素在超时时间内出现在DOM中，则返回 True；否则返回 False。

        示例:
        obj = MyClass()
        obj.等待元素出现(10, 'CSS_SELECTOR', '.my_class')  # 等待直到类名为 .my_class 的元素出现在DOM中，超时时间为 10 秒

        注意:
        - 如果元素在超时时间内出现在DOM中，方法将返回 True。
        - 如果元素在超时时间内未出现在DOM中，方法将返回 False。
        - 如果定位元素失败或超时时间到达，将抛出异常并显示错误信息。
        """
        try:
            WebDriverWait(self.driver, 超时时间).until(
                expected_conditions.presence_of_element_located((self.获取定位器(by), 元素)))
            return False
        except:
            return True

    def 等待元素消失(self, 超时时间, by, 元素):
        """
        等待直到元素从DOM中消失。

        参数:
        - 超时时间 (int): 等待的最长时间，以秒为单位。
        - by (str): 定位策略的字符串表示，应为大写形式，支持的定位策略包括 'ID', 'NAME', 'CLASS_NAME', 'TAG_NAME', 'LINK_TEXT', 'PARTIAL_LINK_TEXT', 'CSS_SELECTOR', 'xp'。
        - 元素 (str): 要等待消失的元素的定位信息，如 ID 名称、类名、标签名、链接文本、部分链接文本、CSS 选择器或 XPath 表达式。

        示例:
        obj = MyClass()
        obj.等待元素出现(10, 'CSS_SELECTOR', '.my_class')  # 等待直到类名为 .my_class 的元素消失在DOM中，超时时间为 10 秒

        注意:
        - 如果元素在超时时间内仍然存在在DOM中，将抛出超时异常。
        - 如果定位元素失败或超时时间到达，将抛出异常并显示错误信息。
        """
        try:
            WebDriverWait(self.driver, 超时时间).until_not(
                expected_conditions.presence_of_element_located((self.获取定位器(by), 元素)))
        except:
            pass

    def 点击元素(self, by, 元素):
        """
        参数:
        by (str): 元素定位策略，例如 'ID', 'NAME', 'CSS_SELECTOR' 等。
        元素 (str): 元素定位信息，例如元素的 ID 名称、CSS 选择器等。

        示例:
        obj = MyClass()
        obj.点击元素('ID', 'myButton')
        """
        try:
            self.查找单个元素(by, 元素).click()
        except Exception as e:
            raise Exception(f'点击元素时出错: {str(e)}')

    def 输入文本(self, by, 元素, 文本):
        """
        参数:
        by: 定位元素的方法，如 'ID', 'NAME', 'CSS_SELECTOR' 等。
        元素: 具体的定位信息，可以是元素的 ID、名称、CSS 选择器等。
        文本: 要输入到输入框中的文本内容。

        示例:
        obj = MyClass()
        obj.输入文本('ID', 'username', 'user123')
        """
        try:
            self.查找单个元素(by, 元素).send_keys(文本)
        except:
            pass

    def 清除元素内容(self, by, 元素):
        """
        参数:
        by: 定位元素的方法，如 'ID', 'NAME', 'CSS_SELECTOR' 等。
        元素: 具体的定位信息，可以是元素的 ID、名称、CSS 选择器等。

        示例:
        obj = MyClass()
        obj.清除元素内容('ID', 'username')
        """
        try:
            elem = self.查找单个元素(by, 元素)
            elem.clear()
        except:
            pass

    def 滚动到元素(self, by, 元素):
        """
        参数:
        by: 定位元素的方法，如 'ID', 'NAME', 'CSS_SELECTOR' 等。
        元素: 具体的定位信息，可以是元素的 ID、名称、CSS 选择器等。

        示例:
        obj = MyClass()
        obj.滚动到元素('ID', 'username')
        """
        try:
            self.driver.execute_script('arguments[0].scrollIntoView(true);', self.查找单个元素(by, 元素))
        except:
            pass

    def 切换到元素窗口(self, by, 元素):
        """
        参数:
        by: 定位元素的方法，如 'ID', 'NAME', 'CSS_SELECTOR' 等。
        元素: 具体的定位信息，可以是元素的 ID、名称、CSS 选择器等。

        示例:
        obj = MyClass()
        obj.切换到元素窗口('ID', 'element_id')
        """
        所有窗口 = self.driver.window_handles
        for 窗口 in 所有窗口:
            self.driver.switch_to.window(窗口)
            try:
                if self.查找多个元素(by, 元素):
                    return True
            except:
                continue
        else:
            print("未找到元素窗口")

    def 随机切换窗口(self):
        """
        随机切换到一个窗口，并输出切换的窗口序号。
        """
        所有窗口 = self.driver.window_handles
        随机窗口 = random.choice(所有窗口)
        窗口序号 = 所有窗口.index(随机窗口) + 1  # 窗口序号从1开始计数
        self.driver.switch_to.window(随机窗口)
        print(f"切换到第 {窗口序号} 个窗口")

    def 获取当前页面标题(self):
        """
        返回值:
        返回当前页面的标题字符串。

        示例:
        title = test.获取当前页面标题()
        """
        return self.driver.title

    def 获取当前URL(self):
        """
        返回值:
        返回当前页面的URL字符串。

        示例用法:
        url = test.获取当前URL()
        """
        return self.driver.current_url

    def 截取屏幕截图(self, 文件路径):
        """
        参数:
        文件路径: 保存截图的完整文件路径，包括文件名和扩展名。

        示例:
        test.截取屏幕截图('screenshots/homepage.png')
        """
        try:
            self.driver.save_screenshot(文件路径)
        except:
            pass

    def 转到URL(self, url):
        """
        参数:
        - url: 要跳转的目标URL地址。

        示例用法:
        test.转到URL('https://www.example.com')
        """
        self.driver.get(url)

    def 刷新页面(self):
        """
        示例用法:
        test.刷新页面()
        """
        self.driver.refresh()

    @staticmethod
    def 启动浏览器():
        """启动浏览器。"""
        print("正在启动浏览器...")
        os.system(r"start .\浏览器\Chrome\chrome.exe --remote-debugging-port=9222")

    def 创建驱动程序(self):
        """使用选项创建Web驱动程序。"""
        用户代理 = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
        选项 = webdriver.ChromeOptions()
        选项.add_argument(f'--user-agent={用户代理}')
        选项.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        self.driver = webdriver.Chrome(service=Service(r'.\浏览器\Chrome\chromedriver.exe'), options=选项)
        self.driver.set_window_size(960, 1045)  # 设置窗口大小
        self.driver.set_window_position(-8, -5)  # 设置窗口位置


class 文件操作:
    @staticmethod
    def 读取文件并去除换行符(文件路径):
        """
        参数:
        文件路径 (str): 要读取的文件的路径。

        返回:
        list: 去除换行符后的文件内容列表。

        示例用法:
        文件路径 = 'example.txt'
        内容列表 = 文件操作.读取文件并去除换行符(文件路径)
        for 内容 in 内容列表:
            print(内容)

        """
        名称列表 = []
        try:
            with open(文件路径, 'r', encoding='utf-8') as 文件:
                for 行 in 文件:
                    # 去除每行末尾的换行符并添加到列表中
                    名称列表.append(行.strip())
        except FileNotFoundError:
            print(f"错误：未找到文件 '{文件路径}'。")
        except Exception as e:
            print(f"错误：发生意外错误：{str(e)}")

        return 名称列表

    @staticmethod
    def 提取所有包含关键字的行(文件路径, 关键字):
        """
        参数:
        文件路径 (str): 要读取的文件的路径。
        关键字 (str): 要搜索的关键字。

        返回:
        list: 所有包含关键字的行组成的列表。

        示例用法:
        文件路径 = 'example.txt'
        关键字 = '关键词'
        包含行列表 = 文件操作.提取所有包含关键字的行(文件路径, 关键字)
        for 行 in 包含行列表:
            print(行)
        """
        包含关键字的行 = []

        try:
            # 打开文件进行读取
            with open(文件路径, 'r', encoding='utf-8') as f:
                # 逐行遍历文件内容
                for line in f:
                    if 关键字 in line:
                        包含关键字的行.append(line.strip())  # 添加去除首尾空白符的行文本到列表中
        except FileNotFoundError:
            print(f"错误: 文件 '{文件路径}' 未找到。")
        except IOError as e:
            print(f"错误: 读取文件 '{文件路径}' 时发生IO错误。详细信息: {e}")

        return 包含关键字的行

    @staticmethod
    def 提取首个包含关键字的行(文件路径, 关键字):
        """
        参数:
        文件路径 (str): 要读取的文件的路径。
        关键字 (str): 要搜索的关键字。

        返回:
        str or None: 第一个包含关键字的行的内容，如果未找到返回 None。

        示例用法:
        文件路径 = 'example.txt'
        关键字 = '关键词'
        首个包含行 = 文件操作.提取首个包含关键字的行(文件路径, 关键字)
        if 首个包含行:
            print(首个包含行)
        else:
            print(f"未在文件 '{文件路径}' 中找到包含关键字 '{关键字}' 的行。")
        """
        try:
            # 打开文件进行读取
            with open(文件路径, 'r', encoding='utf-8') as f:
                # 逐行遍历文件内容
                for line in f:
                    if 关键字 in line:
                        return line.strip()  # 返回去除首尾空白符的行文本
            return None  # 如果未找到包含关键字的行，返回 None
        except FileNotFoundError:
            print(f"错误: 文件 '{文件路径}' 未找到。")
            return None
        except IOError as e:
            print(f"错误: 读取文件 '{文件路径}' 时发生IO错误。详细信息: {e}")
            return None

    @staticmethod
    def 文件去重复(输入文件路径, 输出文件路径):
        """
        参数:
        输入文件路径 (str): 要读取内容的文件路径。
        输出文件路径 (str): 要写入内容的文件路径。

        示例用法:
        输入文件路径 = 'input.txt'
        输出文件路径 = 'output.txt'
        文件操作.文件去重复(输入文件路径, 输出文件路径)
        """
        try:
            '''尝试读取输入文件路径中的内容'''
            with open(输入文件路径, 'r', encoding='utf-8') as f:
                原始内容 = f.readlines()
        except FileNotFoundError:
            print(f"错误: 输入文件路径 '{输入文件路径}' 未找到。")
            return
        except IOError as e:
            print(f"错误: 读取输入文件路径 '{输入文件路径}' 时发生IO错误。详细信息: {e}")
            return

        try:
            '''使用集合去重复'''
            去重后内容 = list(set(原始内容))
            去重后内容.sort(key=原始内容.index)  # 保持原始顺序

            '''尝试将去重后的内容写入输出文件路径'''
            with open(输出文件路径, 'w', encoding='utf-8') as f:
                f.writelines(去重后内容)
        except IOError as e:
            print(f"错误: 写入输出文件路径 '{输出文件路径}' 时发生IO错误。详细信息: {e}")
            return
        print(f"已将文件 '{输入文件路径}' 中的重复行去除，并写入文件 '{输出文件路径}' 中。")

    @staticmethod
    def 写入文件(写入位置, 文件名, 内容):
        """
        参数:
        写入位置 (str): 写入位置，可选 '首' 或 '尾'。
        文件名 (str): 要写入内容的文件路径。
        内容 (str): 要写入的内容。

        示例用法:
        写入位置 = '首'
        文件名 = 'example.txt'
        内容 = '新内容'
        文件操作.写入文件(写入位置, 文件名, 内容)
        """
        try:
            if 写入位置 == '首':
                with open(文件名, 'r+', encoding='utf-8') as 文件:
                    原始内容 = 文件.read()
                    文件.seek(0)  # 将文件指针移到文件开头
                    文件.write(内容 + '\n' + 原始内容)  # 在开头写入内容
            elif 写入位置 == '尾':
                with open(文件名, 'a', encoding='utf-8') as 文件:
                    文件.write(内容 + '\n')  # 在尾部追加内容
            else:
                print(f"未知的写入位置 '{写入位置}'，操作失败。")

            print(f"已成功在文件 '{文件名}' 的 {写入位置} 写入内容。")
        except IOError as e:
            print(f"写入文件 '{文件名}' 时发生错误: {e}")

    @staticmethod
    def 判断内容是否存在文件(文件路径, 目标内容):
        """
        参数:
        文件路径 (str): 要检查的文件路径。
        目标内容 (str): 要查找的内容。

        返回:
        bool: 如果文件中存在包含目标内容的行返回 True，否则返回 False。

        示例用法:
        文件路径 = 'example.txt'
        目标内容 = '目标'
        存在 = 文件操作.判断内容是否存在文件(文件路径, 目标内容)
        if 存在:
            print(f"文件 '{文件路径}' 中存在包含 '{目标内容}' 的行。")
        else:
            print(f"文件 '{文件路径}' 中不存在包含 '{目标内容}' 的行。")
        """
        try:
            # 打开文件进行读取
            with open(文件路径, 'r', encoding='utf-8') as f:
                # 逐行遍历文件内容
                for line in f:
                    if 目标内容 in line:
                        return True
            return False
        except FileNotFoundError:
            print(f"错误: 文件 '{文件路径}' 未找到。")
            return False
        except IOError as e:
            print(f"错误: 读取文件 '{文件路径}' 时发生IO错误。详细信息: {e}")
            return False


class 验证操作:
    @staticmethod
    def 发送请求(url, 参数):
        try:
            response = requests.post(url, data=参数)
            if response.status_code == 200:
                return response.text
            else:
                return f"错误：HTTP状态码 {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"错误：{e}"

    @staticmethod
    def 文心单码登录(软件, 卡密, mac):
        接口 = "http://api.1wxyun.com/?type=17"
        params = {
            'Softid': 软件,
            'Card': 卡密,
            'Version': '1',
            'Mac': mac
        }
        return 验证操作.发送请求(接口, params)

    @staticmethod
    def 文心写入数据(软件, 卡密, 令牌, mac):
        接口 = "http://api.1wxyun.com/?type=19"
        params = {
            'Softid': 软件,
            'UserName': 卡密,
            'Token': 令牌,
            'Data': mac
        }
        return 验证操作.发送请求(接口, params)

    @staticmethod
    def 文心获取数据(软件, 卡密, 令牌, 数据):
        接口 = "http://api.1wxyun.com/?type=21"
        params = {
            'Softid': 软件,
            'UserName': 卡密,
            'Token': 令牌,
            'Type': 数据
        }
        return 验证操作.发送请求(接口, params)

    @staticmethod
    def 权朗科技(id, 卡密, 软件):
        '''
        # 调用权朗科技验证
        参数:
        id:'your_center_id'
        卡密:'your_card_key'
        软件:'your_software'

        示例:
        验证操作.权朗科技(id, 卡密, 软件)
        '''
        url = 'http://api3.2cccc.cc/apiv3/card_login/'
        data = {
            'center_id': id,
            "card": 卡密,
            "software": 软件,
        };
        print(data)
        r = requests.post(url=url, data=data).json()
        print(r)
        if r['code'] == '0':
            print('卡密校验异常')
            exit()
        else:
            print('登录成功')
            pass

    @staticmethod
    def 坚果云验证(账号, 令牌, 卡密):
        '''
        参数：
        账号:坚果云账号
        令牌:坚果云令牌
        卡密，要验证的坚果云卡密号。

        示例:
        坚果云验证(账号,令牌,卡密号)

        '''
        # 获取本机设备号（MAC地址的后12位）
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        # username 为坚果云账号，password 为刚刚创建的密码
        client = Client(base_url='https://dav.jianguoyun.com/dav/',
                        auth=(账号, 令牌))
        服务器卡密 = client.exists(path=f'/卡密/{卡密}')

        if 服务器卡密:
            服务器设备号 = len(client.ls(path=f'/卡密/{卡密}/', detail=False))
            设备号 = client.ls(path=f'/卡密/{卡密}/', detail=False)
            if int(服务器设备号) == 0:
                client.mkdir(f'卡密/{卡密}/{mac}')
                # print('首次登录,验证成功')
                return '首次登录,验证成功'
            else:
                if str(设备号) == str([f'卡密/{卡密}/{mac}']):
                    # print('验证成功')
                    return '验证成功'
                else:
                    # print('验证失败')
                    return '验证失败'
        else:
            # print('卡密错误,验证失败')
            return '卡密错误,验证失败'

    @staticmethod
    def 令牌(key):
        totp = pyotp.TOTP(key)
        print(totp.now())


class 字符操作:
    @staticmethod
    def 替换最后字符(内容, 替换内容):
        '''
        参数:
        内容:要操作的字符串。
        替换内容:替换的字符。

        返回:
        str: 替换后的字符串。

        示例:
        print("替换最后字符示例:", 字符操作.替换最后字符(example_string, '!'))
        '''
        return str(内容)[:-1] + str(替换内容)

    @staticmethod
    def 字符串切片(内容, 首, 尾):
        '''
        参数:
        内容:要操作的字符串。
        首:切片起始位置。
        尾:切片结束位置。

        返回:
        str: 切片后的字符串。

        示例:
        print("字符串切片示例:", 字符操作.字符串切片(example_string, 0, 5))
        '''
        return str(内容)[首:尾]

    @staticmethod
    def 替换内容(内容, 原字符, 替换内容):
        '''
        参数:
        内容: 要操作的字符串。
        原字符: 要替换的原始字符或子字符串。
        替换内容: 替换的新内容。

        返回:
        str: 替换后的字符串。

        示例:
        print("替换内容示例:", 字符操作.替换内容(example_string_world, 'world', 'Python'))
        '''
        return str(内容).replace(原字符, 替换内容)

    @staticmethod
    def 判断字符是否存在(字符, 内容):
        '''
        参数:
        字符: 要查找的字符。
        内容: 要搜索的字符串。

        返回:
        bool: 如果字符存在则返回True，否则返回False。

        示例:
        print("判断字符是否存在示例:", 字符操作.判断字符是否存在('l', example_string))
        '''
        if str(字符) in str(内容):
            return True
        else:
            return False


class 时间操作:
    def __init__(self):
        self._当前时间 = time.time()

    @staticmethod
    def 倒计时(输出方式, timer):
        """
        参数:
        输出方式:一个函数或方法，用于输出倒计时信息。
        timer:倒计时的总时长（以秒为单位）。

        示例:
        时间操作.倒计时(print, 3600)#控制台输出
        时间操作.倒计时(lambda msg: 集合操作.显示(text, msg), 3600)#控件输出
        """
        while timer >= 0:
            hours, remainder = divmod(timer, 3600)  # 计算小时数
            mins, secs = divmod(remainder, 60)  # 计算分钟数和秒数
            timeformat = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)  # 格式化为 HH:MM:SS
            输出方式(f"倒计时:{timeformat}")  # 输出倒计时信息
            time.sleep(1)
            timer -= 1

    def 设置时间(self, 秒):
        """
        参数:
        秒 (int): 要增加的秒数。

        返回:
        int: 更新后的当前时间。

        示例:
        # 假设当前时间是 1625279821.0 (这里是一个示例时间戳)
        obj = MyClass()
        obj.设置时间(60)  # 增加60秒到当前时间
        print(obj.当前时间())  # 输出更新后的当前时间戳
        """
        self._当前时间 += 秒
        return self._当前时间

    def 当前时间(self):
        """
        返回:
        float: 当前时间戳。

        示例:
        obj = MyClass()
        print(obj.当前时间())  # 输出当前时间戳，如 1625279821.0
        """
        return self._当前时间

    @staticmethod
    def 获取时间():
        """
        返回:
        str: 格式化后的本地时间字符串，如 "YYYY-MM-DD HH:MM:SS"。

        示例:
        print(MyClass.获取时间())  # 输出当前的本地时间字符串，如 "2023-07-03 15:30:00"
        """
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def 检查时间(self, 结果):
        """
        参数:
        结果 (str): 要比较的时间字符串，格式为 "YYYY-MM-DD HH:MM:SS"。

        返回:
        bool: 如果当前时间大于等于给定的时间点，则返回 True；否则返回 False。

        示例:
        python
        obj = MyClass()
        结果 = "2023-07-03 12:00:00"  # 假设这是一个未来的时间点
        print(obj.检查时间(结果))  # 输出 True 或者 False，表示当前时间是否大于等于给定的时间点
        """
        结果时间戳 = time.mktime(time.strptime(结果, "%Y-%m-%d %H:%M:%S"))
        return self.当前时间() >= 结果时间戳


class 变量操作:
    def __init__(self, 全局变量, 局部变量):
        """
        初始化变量操作实例。

        :param 全局变量: 全局变量字典，通常使用 `globals()` 获取。
        :param 局部变量: 局部变量字典，通常使用 `locals()` 获取。
        """
        self.全局变量 = 全局变量  # 存储全局变量
        self.局部变量 = 局部变量  # 存储局部变量

    def 检查变量(self, 变量列表, 前缀字典=None, 串联=False, 分隔符=''):
        """
        参数:
        self (object): 类实例本身。
        变量列表 (list): 包含变量名的列表。
        前缀字典 (dict, 可选): 包含前缀和变量名对应关系的字典。例如 {'你好:': '国家', 'msdj:': '省份'}，默认为 None。
        串联 (bool): 指示是否将结果连接成一个字符串。如果为 False，则返回以换行符分隔的字符串。
        分隔符 (str): 用于连接结果的分隔符，仅在 串联 参数为 True 时有效。

        返回:
        str: 添加前缀后的变量值字符串，根据 串联 参数选择格式。

        示例:
        # 创建类实例
        obj = MyClass()
        # 定义变量列表和前缀字典
        变量列表 = ['变量1', '变量2']
        前缀字典 = {'你好:': '国家', 'msdj:': '省份'}
        # 调用方法并打印结果
        print(obj.检查变量(变量列表, 前缀字典=前缀字典, 串联=False))
        # 输出:
        # 国家变量1
        # 省份变量2
        print(obj.检查变量(变量列表, 前缀字典=前缀字典, 串联=True, 分隔符=' | '))
        # 输出: 国家变量1 | 省份变量2
        """
        结果 = []  # 用于存储最终结果
        for 变量 in 变量列表:
            # 从局部变量开始查找，如果找不到则从全局变量中查找
            变量值 = self.局部变量.get(变量, self.全局变量.get(变量, None))
            if 变量值 is not None:
                if 前缀字典 and 变量 in 前缀字典:
                    前缀 = 前缀字典[变量]
                    结果.append(f"{前缀}{变量值}")
                else:
                    结果.append(f"{变量值}")

        # 根据是否连接参数返回结果
        return 分隔符.join(结果) if 串联 else '\n'.join(结果)


class 集合操作:
    @staticmethod
    def 生成微信二维码名片(名字, 电话, 地址, 邮箱, 生日, 二维码图片名字, 二维码大小):
        '''
        参数:
        名字 (str): 名字信息。
        电话 (str): 电话号码信息。
        地址 (str): 地址信息。
        邮箱 (str): 邮箱信息。
        生日 (str): 生日信息。
        二维码图片名字 (str): 生成的二维码图片文件名。
        二维码大小 (int): 二维码图片的缩放比例。

        示例:
        # 调用生成微信二维码名片方法
        名字 = "John Doe"
        电话 = "123456789"
        地址 = "123 Main St, City"
        邮箱 = "john.doe@example.com"
        生日 = "1990-01-01"
        二维码图片名字 = "john_doe_qr.png"
        二维码大小 = 5
        生成微信二维码名片(名字, 电话, 地址, 邮箱, 生日, 二维码图片名字, 二维码大小)
        '''
        二维码 = helpers.make_mecard(name=名字, phone=电话, pobox=地址, email=邮箱, birthday=生日)
        二维码.save(二维码图片名字, scale=二维码大小)  # 规定图片后缀png,设置图片大小

    @staticmethod
    def 邮件(用户, 授权, 地址, 主题, 内容):
        '''
        参数:
        用户 (str): 发送邮件的用户名。
        授权 (str): 发送邮件的授权码。
        地址 (str or list): 收件人的邮箱地址，可以是单个地址或地址列表。
        主题 (str): 邮件主题。
        内容 (str): 邮件内容。

        示例:
        # 调用发送邮件方法
        用户 = "your_email@example.com"
        授权 = "your_password_or_app_password"
        地址 = ["recipient1@example.com", "recipient2@example.com"]
        主题 = "测试邮件"
        内容 = "这是一封测试邮件的内容。"
        邮件(用户, 授权, 地址, 主题, 内容)
        '''
        授权 = yagmail.SMTP(user=用户, password=授权, host='smtp.qq.com')
        授权.send(地址, 主题, 内容)
        授权.close()

    @staticmethod
    def 显示(text_widget, *args, sep=' ', end='\n', file=None):
        '''
        参数:
        *args -- 要显示的内容，可以是多个参数，会被连接成一个字符串。
        sep -- 连接多个参数时使用的分隔符，默认为单个空格。
        end -- 插入到 text_widget 后的换行符，默认为换行。
        file -- 可选，指定打印输出到文件的对象，默认为 None（打印到控制台）。

        示例:
        集合操作.显示(text, "Hello", "world!", sep='-', end='...')
        '''
        text_widget.configure(state=tkinter.NORMAL)
        内容 = ">>>" + sep.join(map(str, args)) + end  # 将所有参数转换为字符串并连接起来
        print(内容, end='', file=file)  # 在控制台打印内容
        text_widget.insert("end", 内容)
        text_widget.see("end")
        text_widget.configure(state=tkinter.DISABLED)


class 微信操作:
    CLICK_URL = ''  # 填写您需要点击跳转的 URL

    def 获取访问令牌(self, app_id, app_secret):
        '''
        参数：
        app_id: 应用的 App ID。
        app_secret: 应用的 App Secret。

        返回值：
        如果成功获取到 access_token，则返回该 access_token；否则返回 None。
        '''
        url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}"
        resp = requests.get(url)
        result = resp.json()
        if 'access_token' in result:
            return result["access_token"]
        else:
            print(result)
            return None

    def 获取发送数据(self, json_data, touser, template_id, click_url):
        '''
        参数：
        json_data: 包含消息内容的 JSON 数据。
        touser: 接收消息的用户列表。
        template_id: 模板消息的 ID。
        click_url: 点击跳转的 URL。

        返回值：
        返回一个字典，包含构造好的发送数据。
        '''
        return {
            "touser": touser,
            "template_id": template_id,
            "url": click_url,
            "topcolor": "#FF0000",
            "data": {
                "name": {
                    "value": json_data["name"],
                    "color": "#173177"
                },
                "code": {
                    "value": json_data["code"],
                    "color": "#173177"
                },
            }
        }

    def 发送消息(self, json_data, app_id, app_secret, touser, template_id, click_url):
        '''
        参数：
        json_data: 包含消息内容的 JSON 数据。
        app_id: 应用的 App ID。
        app_secret: 应用的 App Secret。
        touser: 接收消息的用户列表。
        template_id: 模板消息的 ID。
        click_url: 点击跳转的 URL。

        功能：
        调用 get_access_token() 获取 access_token。
        调用 get_send_data() 构造发送数据。
        发送 HTTP POST 请求，将消息发送给指定的用户。
        '''
        access_token = self.获取访问令牌(app_id, app_secret)
        if not access_token:
            print("获取 access_token 失败")
            return
        url = f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}"
        for user in touser:
            send_data = self.获取发送数据(json_data, user, template_id, click_url)
            data = json.dumps(send_data)
            resp = requests.post(url, data=data)
            result = resp.json()
            if result["errcode"] == 0:
                print(f"消息发送成功给用户: {user}")
            else:
                print(f"消息发送失败给用户: {user}, 错误信息: {result}")

    def 推送消息(app_id, app_secret, template_id, users, 内容):
        '''
        参数：
        users: 接收消息的用户列表。
        内容: 要发送的消息内容。

        示例：
        推送消息(users, 内容)
        #其中 users 是接收消息的用户列表，内容 是要发送的消息内容。
        '''
        wechat = 微信操作()
        json_data = {"name": 时间操作.获取时间(), "code": 内容}
        wechat.发送消息(
            json_data=json_data,
            app_id=app_id,
            app_secret=app_secret,
            touser=users,
            template_id=template_id,
            click_url=wechat.CLICK_URL
        )
