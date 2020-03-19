#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Administrator
@file: demo001.py
@time: 2020/03/{DAY}
"""
import json

data=['[{"id":1039272}]']
print(type(data),data)
print('*' * 100)
data1 = json.loads(data[0])
print(type(data1),data1)
print('*' * 100)
# all_result = json.dumps(res[1])
# print(all_result)
