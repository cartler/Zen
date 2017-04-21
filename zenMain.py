#!/usr/bin/python
#-*- coding: UTF-8 -*-

import zenConfig
import zenCSV

def main():
    testDataFile = zenConfig.config['INPUT']['InputFile']
    print('测试数据: ', testDataFile)

    baseUrl = zenConfig.config['INPUT']['BaseURL']
    print('baseUrl: ', baseUrl)

    zenCSV.loadFile(testDataFile)
    print(zenCSV.pd)

    urls = zenCSV.prepareUrls(baseUrl)
    print(urls)



if __name__ == '__main__':
    main()