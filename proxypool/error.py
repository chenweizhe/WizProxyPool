# -*- coding: utf-8 -*-
# @Time    : 18-4-10 下午9:26
# @Author  : pythonZhe
# @Email   : 18219111730@163.com
# @File    : error.py
# @Software: PyCharm

class ResourceDepletionError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return repr('the proxypool source is exhausted')

class PoolEmptyError(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __str__(self):
        return  repr('The proxyPool is empty')

