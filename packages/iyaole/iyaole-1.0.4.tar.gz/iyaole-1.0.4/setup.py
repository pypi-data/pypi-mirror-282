import codecs
import os

from setuptools import find_packages, setup

# these things are needed for the README.md show on pypi
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '1.0.4'
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
        'getch; platform_system=="windows"'
    ],
    keywords=['python', 'windows'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)