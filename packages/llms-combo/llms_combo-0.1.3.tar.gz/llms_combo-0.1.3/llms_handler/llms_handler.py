#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/3 上午9:34
# @Author  : haochonglei
# @File    : llms_handler.py
# @Software: PyCharm
from llm.kimi.kimi import KIMI



def hello():
    return "Hello, World!"

if __name__ == '__main__':
    kimi = KIMI("sk-bTvzzRgAtMMfvSgXWmt54xjhZGzud652h4V1Seok8hNqROV8")

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]
    res = kimi.direct(messages)
    print(res)