#!/usr/bin/python
#-*- coding: UTF-8 -*-

# 参考 https://docs.python.org/3.6/library/configparser.html

import configparser

config = configparser.ConfigParser()
# config.sections()
config.read('config.ini')

if __name__ == '__main__':
    # print(config['LOG']['LogFile'])

    # 显示所有配置项
    for section in config.sections():
        for option in config.options(section):
            value = config[section][option]
            print(section,' = ', value)
