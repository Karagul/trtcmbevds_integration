# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

# get version from __version__ variable in trtcmbevds_integration/__init__.py
from trtcmbevds_integration import __version__ as version

setup(
    name='trtcmbevds_integration',
    version=version,
    description='TR Turkish Central Bank EVDS web services integration of economic data for ErpNext',
    author='Framras AS-Izmir',
    author_email='bilgi@framras.com.tr',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
