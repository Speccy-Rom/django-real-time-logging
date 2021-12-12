import os
import sys
import setuptools

__author__ = 'Spiridonov Roman <email.speccy.rom@gmail.com>'
__version__ = '0.21'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='django-rtl',
    version=__version__,
    install_requires=['django>=1.11'],
    author='Spiridonov Roman',
    author_email='email.speccy.rom@gmail.com>',
    description='Useful and simple real-time logging middleware for django projects.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/Speccy-Rom/django-real-time-logging",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
