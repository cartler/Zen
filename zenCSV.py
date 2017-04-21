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

    print(list(pd.columns))

    for index in range(len(pd)):
        # print(pd.loc[0,'com'])
        params = list(pd.columns)
        aa = baseUrl.format(com='111',id='222')
        print(aa)

    return urls


if __name__ == '__main__':
    pd = pandas.read_csv('example_data.csv')
    # pdi = pd.reindex
    print(pd['com'])
    # val = pd.iloc[0]
    # print(val)

