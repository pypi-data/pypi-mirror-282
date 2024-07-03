#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/3 上午9:33
# @Author  : haochonglei
# @File    : __init__.py
# @Software: PyCharm
from .llms_handler import hello
from .llm.kimi.kimi import KIMI

# 设置包的版本
__version__ = "0.1.2"

kimi_direct = KIMI.direct()
# 定义包的公共API
__all__ = ["hello", "kimi_direct"]
