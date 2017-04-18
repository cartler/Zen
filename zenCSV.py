#!/usr/bin/python
#-*- coding: UTF-8 -*-

import numpy
import pandas

if __name__ == '__main__':
    pd = pandas.read_csv('example_data.csv')
    # pdi = pd.reindex
    print(pd['com'])
    # val = pd.iloc[0]
    # print(val)

