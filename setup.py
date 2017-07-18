#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
"""
打包的用的setup必须引入，
"""

VERSION = '1.0.0'

setup(name='wp',
      version=VERSION,
      description='Tell your leader what you did this week',
      long_description='just enjoy',
      classifiers=[],
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='python workreport terminal',
      author='nix',
      author_email='xiaoyao.ning@gmail.com',
      url='https://github.com/WellerQu/weekday',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'ConfigParser',
          'mistune',
          'colorama',
          'cython',
          'pydash',
      ],
      entry_points={
          'console_scripts': [
              'wp = weekday.main:main'
          ]
      },
      )
