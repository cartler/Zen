#!/usr/bin/python
#-*- coding: UTF-8 -*-

# 参考 http://docs.python-requests.org/en/master/user/quickstart/
# 认证 http://docs.python-requests.org/en/master/user/authentication/

import requests

if __name__ == '__main__':
    r = requests.get('https://api.github.com/events')
    print(r.content)