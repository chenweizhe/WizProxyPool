# -*- coding: utf-8 -*-
# @Time    : 18-4-10 下午9:24
# @Author  : pythonZhe
# @Email   : 18219111730@163.com
# @File    : api.py
# @Software: PyCharm
from flask import Flask, g
from proxypool.db import RedisClient

__all__ = ['app']

app =Flask(__name__)

def get_conn():
    '''打开一个redis连接'''
    if not hasattr(g, 'redis_client'):
        g.redis_client = RedisClient()
    return g.redis_client

@app.route('/')
def index():
    return  '<h2>Welcome to My Proxy Pool System</h2>'

# 通过本地地址获取代理地址
@app.route('/get')
def get_proxy():
    conn = get_conn()
    return conn.pop()

@app.route('/count')
def get_counts():
    '''获取当前代理池中代理数量'''
    conn = get_conn()
    return str(conn.queue_len)


if __name__ == '__main__':
    app.run()