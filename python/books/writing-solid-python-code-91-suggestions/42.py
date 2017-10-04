#coding:utf8
"""
使用pandas处理大型csv文件
"""
import csv
# DictWriter
'''
with open('test.csv', 'wb') as csv_file:
    #设置列名称
    FILEDS = ['Transaction_Date', 'Product', 'Price', 'Payment_Type']
    writer = csv.DictWriter(csv_file, fieldnames=FILEDS)
    writer.writerow(dict(zip(FILEDS, FILEDS)))
    d = {'Transaction_Date':'1/2/09', 'Product':'product1', 'Price':'1200', 'Payment_Type':'Mastercard'}
    writer.writerow(d)
with open('test.csv', 'rb') as csv_file:
    for d in csv.DictReader(csv_file):
        print d
'''

"""
pandas :
Series: 类似于数组的带索引的一维数据结构，支持的类型与numpy兼容
obj.values()  : 获取值
obj.index()   : 获取索引
"""
from pandas import Series
obj1 = Series([1, 'a', (1, 2), 3], index=['a', 'b', 'c', 'd'])
print obj1


'''
DataFrame:  类似于电子表格，数据为排好序的数据列的集合，每一列为不同的数据类型
'''
data = {'OrderDate':['1-6-10', '1-23-10', '2-9-10', '2-26-10', '2-15-10'],
        'Region': ['East', 'Central', 'Central', 'West', 'East'],
        'Req': ['Jones', 'Kivell', 'Jardine', 'Gill', 'Sorvino']}

from pandas import DataFrame
print DataFrame(data, columns=['OrderDate', 'Region', 'Req'])

import pandas as pd
# 指定读取的行数，列的名字
df = pd.read_csv("SampleData.csv", nrows=4, usecols=['OrderDate', 'Item', 'Total'], skiprows=[1,2], delimiter=',')
print df
# 设置CSV文件与excel兼容
dia=csv.excel()
dia.delimiter="|"

# 对文件进行分块处理并返回一个可迭代的对象
# pd.read_table()

# 文件格式相似的时候，支持多个文件合并处理

# pandas其底层的很多的算法采用Cython实现运行速度较快
# pandas在专业的数据处理与分析领域，得到应用

