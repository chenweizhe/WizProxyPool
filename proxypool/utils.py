# -*- coding: utf-8 -*-
# @Time    : 18-4-10 下午9:28
# @Author  : pythonZhe
# @Email   : 18219111730@163.com
# @File    : utils.py
# @Software: PyCharm
import requests
import asyncio
import aiohttp
from requests.exceptions import ConnectionError
from fake_useragent import UserAgent,FakeUserAgentError
import random

def get_page(url,options={}):

    try:
        ua = UserAgent()
    except FakeUserAgentError:
        pass

    base_headers={
        'User-Agent': ua.random,
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }

    headers = dict(base_headers, **options)
    print('Getting',url)
    try:
        r = requests.get(url, headers=headers)
        print('Getting result', url, r.status_code)
        if r.status_code == 200:
            return r.text
    except ConnectionError:
        print('Crawling Failed',url)
        return None


class Downloader(object):
    '''异步下载器，对代理源进行异步抓取，容易被禁'''

    def __init__(self, urls):
        self.urls = urls
        self._htmls = []

    async def download_single_page(self,url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                self._htmls.append(await resp.text())

    def download(self):
        loop = asyncio.get_event_loop()
        tasks = [self.download_single_page(url) for url in self.urls]
        loop.run_until_complete(asyncio.wait(tasks))

    @property
    def htmls(self):
        self.download()
        return self._htmls
