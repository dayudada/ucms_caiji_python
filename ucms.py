#!/usr/bin/env python
# -*- coding:utf-8 -*-

# UCMS采集python推送模块
# by 大雨
# UCMS 官网 uuu.la
import requests
import re

def post(url,data):
    callback = {}
    try:
        r = requests.post(url, data)
        result = r.text
        # print(result)
        if result == 'ok':
            callback['code'] = 1
            callback['msg'] = '推送成功'
            return callback
        elif result == 'no cid':
            callback['code'] = 2
            callback['msg'] = '栏目cid参数不能为空'
            return callback
        elif result == 'channel not exist':
            callback['code'] = 3
            callback['msg'] = '栏目不存在'
            return callback
        elif ('field list' in result) == True:
            txt = re.search(r'\'(.*?)\'', result)
            callback['code'] = 4
            callback['msg'] = '栏目字段 ' + str(txt.group(1)) + ' 不存在'
            return callback
        elif ('404 Not Found' in result) == True:
            callback['code'] = 5
            callback['msg'] = '采集接口网址错误'
            return callback
        else:
            callback['code'] = 6
            callback['msg'] = '网络错误或其它未知错误'
            return callback
    except:
        callback['code'] = 7
        callback['msg'] = '网址无法访问'
        return callback

def post_list(url,dataarry):
    callback = {}
    a =0
    for data in dataarry:
        r=post(url,data)
        if r['code']==1:
            a=a+1
    callback['code']=1
    callback['successnum']=a
    return callback
