from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.2'
DESCRIPTION = 'Hi, are you ready for experiencing the first Indian search engine "Surya"? I know it is not that advanced, but it is my first module. Here are all the functions of my search engine: search different search engine results to give you results on one engine, read aloud function for those who want to hear it in English right now, which also looks good.'

# Setting up
setup(
    name="IndianSearchengineSurya",
    version=VERSION,
    author="Suraj sharma",
    author_email="Surajsharma963472@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'PyQtWebEngine',
        'pyttsx3',
        'requests',
        'bs4'
    ],
    keywords=['python', 'web', 'Search engine', 'python tutorial', 'Suraj Sharma'],
)