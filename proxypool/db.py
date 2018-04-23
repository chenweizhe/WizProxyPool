# -*- coding: utf-8 -*-
# @Time    : 18-4-10 下午9:24
# @Author  : pythonZhe
# @Email   : 18219111730@163.com
# @File    : db.py
# @Software: PyCharm
from proxypool.error import PoolEmptyError
from proxypool.setting import HOST, PORT, PASSWORD
import redis
from redis import Redis

class RedisClient(object):
    def __init__(self, host=HOST, port=PORT):
        if PASSWORD:
            self._db = redis.Redis(host=host, port=port, password=PASSWORD)
        else:
            self._db = redis.Redis(host=host, port=port)

    def get(self, count=1):
        '''从redis中获取代理地址'''
        proxies = self._db.lrange('proxies',0,count-1)
        self._db.ltrim('proxies', count, -1)
        return proxies

    # 将获取的代理存到redis数据库
    def put(self,proxy):
        self._db.rpush('proxies',proxy)

    '''从右往左取出代理地址'''
    def pop(self):
        try:
            return self._db.rpop('proxies').decode('utf-8')
        except:
            raise PoolEmptyError

    @property
    def queue_len(self):
        '''获取数据库长度'''
        return self._db.llen('proxies')

    def flush(self):
        '''刷新数据库'''
        self._db.flushall()

if __name__ == '__main__':
    conn = RedisClient()

