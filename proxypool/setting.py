# -*- coding: utf-8 -*-
# @Time    : 18-4-10 下午9:27
# @Author  : pythonZhe
# @Email   : 18219111730@163.com
# @File    : setting.py
# @Software: PyCharm
# @details : 设置文件

# Redis数据库的地址和接口
HOST = 'localhost'
PORT = 6379
PASSWORD = '123456'

# 获得代理测试时间界限
get_proxy_timeout = 10

# 代理池数量界限
POOL_LOWER_THRESHOLD = 20
POOL_UPPER_THRESHOLD = 60

# 检查周期
VALID_CHECK_CYCLE = 60
POOL_LEN_CHECK_CYCLE = 20

# 测试api
TEST_API = 'https://www.baidu.com'
