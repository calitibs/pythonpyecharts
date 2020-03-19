#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:Administrator
@file: virus  distribution.py
@time: 2020/03/{DAY}
"""
'''
django+pyecharts实现疫情数据可视化web页面
来自丁香园、搜狗及百度的疫情实时动态展示页
https://ncov.dxy.cn/ncovh5/view/pneumonia
'''

import requests
import re
import json
import time
from pymongo import MongoClient


def insert_item(item, type_):
    '''
    插入数据到mongodb，item为要插入的数据，type_用来选择collection
    '''
    databaseIp = '127.0.0.1'
    databasePort = 27017
    client = MongoClient(databaseIp, databasePort)
    mongodbName = 'dingxiang'
    db = client[mongodbName]  # 拿到指定库，没有则创建
    if type_ == 'dxy_map':
        # 更新插入
        print('{} 正在上传数据库'.format(type_))
        db.dxy_map.update({'id': item['provinceName']}, {'$set': item}, upsert=True)

    elif type_ == 'sogou':
        # 直接插入
        print('{} 正在上传数据库'.format(type_))
        db.sogou.insert_one(item)

    else:
        # 更新插入
        print('{} 正在上传数据库'.format(type_))
        db.baidu_line.update({}, {'$set': item}, upsert=True)

    print(type_, '插入成功')
    client.close()


def dxy_spider():
    '''
    丁香园爬取，获取各省份的确诊数，用来做地理热力图
    '''
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'
    r = requests.get(url)
    r.encoding = 'utf-8'
    res = re.findall('tryTypeService1 =(.*?)}catch', r.text, re.S)
    # data=['[{"id":1039272}]']
    if res:
        # 获取数据的修改时间
        time_result = json.loads(res[0])
        # data=[{'id': 1039272}]

    # 获取省份确诊人数数据
    res = re.findall('getAreaStat =(.*?)}catch', r.text, re.S)
    print(res)
    if res:
        all_result = json.loads(res[0])
    count = re.findall('getStatisticsService =(.*?)}catch', r.text, re.S)
    if count:
        count_res = json.loads(count[0])
        count_res['crawl_time'] = int(time.time())
        if count_res.get('confirmedIncr') > 0:
            count_res['confirmedIncr'] = '+' + str(count_res['confirmedIncr'])
        if count_res.get('seriousIncr') > 0:
            count_res['seriousIncr'] = '+' + str(count_res['seriousIncr'])
        if count_res.get('curedIncr') > 0:
            count_res['curedIncr'] = '+' + str(count_res['curedIncr'])
        if count_res.get('deadIncr') > 0:
            count_res['deadIncr'] = '+' + str(count_res['deadIncr'])
        insert_item(count_res, 'dxy_count')


    for times in time_result:
        for item in all_result:
            if times['provinceName'] == item['provinceName']:
                # 因为省份确诊人数的部分没有时间，这里将时间整合进去
                item['createTime'] = times['createTime']
                item['modifyTime'] = times['modifyTime']
                insert_item(item, 'dxy_map')



def sogou_spider():
    '''
    搜狗爬虫，获取所有确诊数、治愈数等，用在导航栏直接显示
    '''
    url = 'http://sa.sogou.com/new-weball/page/sgs/epidemic'
    r = requests.get(url=url)
    r.encoding = 'utf-8'
    sum_res = re.findall('"domesticStats":({"tim.*?}})', r.text)

    if sum_res:
        sum_result = json.loads(sum_res[0])
        # 增加一个爬取时间字段
        sum_result['crawl_time'] = int(time.time())
        insert_item(sum_res, 'sogou')


def baidu_spider():
    '''
    百度爬虫，爬取历史数据，用来画折线图
    '''
    url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'
    r = requests.get(url=url)
    res = re.findall('"degree":"3408"}],"trend":(.*?]}]})', r.text, re.S)
    data = json.loads(res[0])
    print(data)
    insert_item(data, 'baidu_line')


if __name__ == '__main__':
    # dxy_spider()
    sogou_spider()
    # baidu_spider()
