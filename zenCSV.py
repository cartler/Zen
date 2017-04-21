#!/usr/bin/python
#-*- coding: UTF-8 -*-

import numpy
import pandas

pd = None

def loadFile(fileName):
    global pd
    pd = pandas.read_csv(fileName)

def prepareUrls(baseUrl):
    urls = []
    global pd

    for index in range(len(pd)):
        # print(pd.loc[0,'com'])
        param = pd.ix[index].to_dict()
        url = baseUrl.format(param = param)
        urls.append(url)

    return urls


if __name__ == '__main__':
    pd = pandas.read_csv('example_data.csv')
    # pdi = pd.reindex
    # print(pd['com'])
    print(pd.ix[0].to_dict())
    # val = pd.iloc[0]
    # print(val)

