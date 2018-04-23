# -*- coding: utf-8 -*-
# @Time    : 18-4-10 下午9:17
# @Author  : pythonZhe
# @Email   : 18219111730@163.com
# @File    : run.py
# @Software: PyCharm

from proxypool.api import app
from proxypool.schedule import Schedule
from proxypool.db import RedisClient
def main():
    s = Schedule()
    s.run()
    app.run()


if __name__ == '__main__':
    main()