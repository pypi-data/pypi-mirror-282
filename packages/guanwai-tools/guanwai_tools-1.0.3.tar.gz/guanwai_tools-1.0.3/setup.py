# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='guanwai_tools',
    version='1.0.3',
    packages=find_packages(),
    description='A simple example package',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    # url='http://github.com/yourusername/my_package',
    author='gaunwai',
    author_email='171391909@qq.com',
    license='MIT',
    install_requires=[
        "pymongo",
    ],
    classifiers=[
    ]
)
