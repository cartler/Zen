#!/usr/bin/python
#-*- coding: UTF-8 -*-

import zenConfig
import zenCSV
import zenRequest

def main():
    testDataFile = zenConfig.config['INPUT']['InputFile']
    print('测试数据: ', testDataFile)

    baseUrl = zenConfig.config['INPUT']['BaseURL']
    print('baseUrl: ', baseUrl)

    zenCSV.loadFile(testDataFile)
    print(zenCSV.pd)

    urls = zenCSV.prepareUrls(baseUrl)
    print(urls)

    for url in urls:
        r = zenRequest.requests.get(url)
        print(r.content)



if __name__ == '__main__':
    main()

    # BaseURL = 'http://www.kuaidi100.com/query?type={params[com]}&postid={params[id]}'
    # haha = {'com':'zhongtong', 'id':'111222333'}
    # a = BaseURL.format(params=haha)
    # print(a)
