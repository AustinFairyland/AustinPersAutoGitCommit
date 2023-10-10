# coding: utf8
""" 
@File: __init__.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-09-30
"""

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from .AutoGitCommit.operations import OperationClass

__all__ = [
    'OperationClass'
]
