# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 21:40:03 2024

@author: Subham Divakar
"""

from setuptools import setup, find_packages

setup(
    name='sdscmt',
    version='0.1.3',
    description='SDSCMT(Secure Data SSL Certificate Management Tool) It is comprehensive tool for generating, renewing, storing and monitoring Self Signed SSL certificates, ensuring enhanced security and streamlined management.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Subham Divakar',
    author_email='shubham.divakar@gmail.com',
    url='https://github.com/shubham10divakar/sdscmt',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'pyOpenSSL',
    ],
    entry_points={
        'console_scripts': [
            'sdscmt=generate_cert:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
