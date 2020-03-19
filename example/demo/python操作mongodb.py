#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:Administrator
@file: python操作mongodb.py
@time: 2020/03/{DAY}
"""
from pymongo import MongoClient

client = MongoClient(host='127.0.0.1',port=27017)

# 获取所有库
# dbs = client.list_databases()
dbs = client.database_names()
print(dbs)
# for i in dbs:
#     print(i)
# print(next(dbs))
# print(next(dbs))
# print(next(dbs))
# print(next(dbs))

# # 拿到指定库
db = client['students']
print(db)
#
# # 获取所有集合
tables = db.collection_names()
print(tables)
#
# # 获取一个集合, 指定得集合
tab = db['stu']
print(tab)

# 获取指定集合
tbs = db.get_collection(name='tz')
print(tbs)
#
# # 增
# dict = [
#     {'name':'大数据','learn':'db1','age':10},
#     {'name':'运维','learn':'db2','age':25},
#     {'name':'人工智能','learn':'db3','age':18},
#     {'name':'机器学习','learn':'db4','age':22},
#     {'name':'爬虫','learn':'db5','age':38}
# ]
# # datas = tab.insert_many(dict)
#
# b = {
#     'name':'hello world','age':18,
#     'course':{'python':'s1','web':'s2','c++':'s3'},
#     'habby':['music','dance','video']
# }
# # tab.insert(b)
#
# # 查询
# res = tab.find()
# print(res)
# # for i in res:
# #     print(i)
# #  获取满足条件得一条值
# res1 = tab.find_one()
# print(res1)