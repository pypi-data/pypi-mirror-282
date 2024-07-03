import codecs
import os

from setuptools import find_packages, setup

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '7'
DESCRIPTION = 'Encapsulation'
LONG_DESCRIPTION = 'Encapsulation'

# Setting up
setup(
    name="iyaole",
    version=VERSION,
    author="浮生",
    author_email="iyaole@vip.qq.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'pyautogui==0.9.54',
        'requests==2.32.3',
        'pyotp==2.9.0',
        'helpers==0.2.0',
        'yagmail==0.15.293',
        'keyboard==0.13.5',
        'numpy==2.0.0',
        'selenium==4.21.0',
        'opencv_python==4.10.0.84',
        'pyinstaller==6.8.0',
        'pywin32==306',
        'pywin32_ctypes==0.2.2',
        'twine==5.1.1',
        'webdav4==0.9.8'
    ],
    keywords=['python', 'windows'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)