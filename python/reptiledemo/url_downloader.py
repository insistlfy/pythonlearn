# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:lfy
@file: url_downloader.py
@time: 2021-04-14 下午4:44
@description: url_downloader
"""

from urllib3.poolmanager import PoolManager
from urllib3 import HTTPResponse


def down_html(url, encoding='UTF-8', method='get'):
    http = PoolManager()
    # res: HTTPResponse = http.request(method, url)
    res: HTTPResponse = http.request(method=method, url=url)

    if res.status == 200:
        # return res.data.decode(encoding)
        return res.data.decode(encoding=encoding)
    else:
        return None


if __name__ == '__main__':
    print(down_html('http://www.baidu.com'))
