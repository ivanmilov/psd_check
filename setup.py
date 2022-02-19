#!/usr/bin/env python

from setuptools import setup

setup(name='psd_check',
      version='1.0',
      description='Check and rename layout names',
      author='Ivan Milov',
      url='https://github.com/ivanmilov/psd_check',
      scripts=[
          'psd_check'
      ],
      install_requires=[
          'psd_tools',
          'tkinter',
          'tkinterdnd2'
      ],
      )
