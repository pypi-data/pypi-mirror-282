from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.4'
DESCRIPTION = 'avi'
LONG_DESCRIPTION = 'A package to perform arithmetic operations'

# Setting up
setup(
    name="suryaengineforsearch",
    version=0.1,
    author="Suraj Sharma",
    author_email="Surajsharma963472@gmail.com",
    description="Hi, are you ready for experiencing the first Indian search engine Surya? I know it's not that advanced, but it's my first module. Here are all the functions of my search engine: search different search engine results to give you results on one engine, read aloud function for those who want to hear it in English right now, which also looks good.",
    packages=find_packages(),
    install_requires=[
        "requests",
        "PyQt5",
        "beautifulsoup4",
        "pyttsx3",
        "qtwidgets",
        "PyQtWebEngine"
    ],
    keywords=['Surya', 'Coding', 'Search engine', 'python ', 'Suraj sharma'
    ]
)
