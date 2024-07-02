# -*- coding: utf-8 -*-
"""
@Author: zhaoqingchen
@Email: zqcchris@163.com
@Time: 2024/7/2 08:39
"""
from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize

# 定义Cython扩展模块
extensions = [
    Extension("AISummary", ["gptsummary.pyx"]),
    # 可以添加更多的扩展模块
]

setup(
    name='gptsummary',
    version='0.0.1',
    packages=find_packages(),
    ext_modules=cythonize(extensions),
    # 其他元数据
    author='Ainancer',
    # author_email='your.email@example.com',
    description='AI-Powered Summary Tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # url='https://github.com/yourusername/your_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    # 包含非Python文件
    package_data={
        'your_package': ['*.so', '*.pyi', "*.pyd"],
    },
    include_package_data=True,
)