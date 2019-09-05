#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 安装ucms采集推送库 pip install ucms

# 引用ucms采集推送库
from ucms import ucms

# 单文章推送函数
# ucms.post(url,data)
# 成功返示例: {'code': 1, 'msg': '推送成功'}
# code 状态码: 1推送成功 2栏目cid参数不能为空 3栏目不存在 4栏目某个字段不存在(msg返回信息中会说明是哪个字段) 5采集接口网址错误 6网络错误或其它未知错误 7网址无法访问

# 多文章推送
# ucms.post_list(url,data)
# 成功返回示例: {'code': 1, 'successnum': 4}
# code 状态码: 1推送成功
# successnum 成功推送条数
# 如果 成功推送条数为0 而实际推送了多条数据，说明推送失败，请用单文章推送测试错误原因

# 采集推送接口url
url='http://127.0.0.1/post.php'

# 单文章推送演示
data={}
data['cid']=1
data['title']='单文章推送演示1'
data['content']='这是文章内容这是文章内容这是文章内容这是文章内容这是文章内容'

r=ucms.post(url,data)
print(r)
print(r['code'])
print(r['msg'])

# 多文章推送演示
data={}
datalist=[]
data['cid']=1
data['title']='多文章推送演示1'
data['content']='这是多文章推送演示文章内容这是文章内容这是文章内容这是文章内容这是文章内容'
datalist.append(data)
data['cid']=1
data['title']='多文章推送演示2'
data['content']='这是多文章推送演示文章内容这是文章内容这是文章内容这是文章内容这是文章内容'
datalist.append(data)
data['cid']=1
data['title']='多文章推送演示3'
data['content']='这是多文章推送演示文章内容这是文章内容这是文章内容这是文章内容这是文章内容'
datalist.append(data)
data['cid']=1
data['title']='多文章推送演示4'
data['content']='这是多文章推送演示文章内容这是文章内容这是文章内容这是文章内容这是文章内容'
datalist.append(data)

r=ucms.post_list(url,datalist)
print(r)
print(r['code'])
print('成功推送数: ',str(r['successnum']))
