# UCMS 采集接口python推送库

by:大雨

UCMS采集接口python推送库,用于python将采集内容推送到UCMS上

UCMS是一款UCMS是一款简单的开源内容管理系统，可以非常方便的通过它来快速开发各种各种企业站、文章站、站群系统。
**UCMS官网** [http://uuu.la](http://uuu.la)

而UCMS采集接口python推送库是UCMS采集插件的一个python采集辅助库，让你用python将采集数据轻松的推送到UCMS上

使用本库请确保您的网站系统使用的是UCMS，并且安装了采集插件。post.php为官方采集插件([采集插件官方使用说明](http://uuu.la/help/56.html))，百度站长+熊掌号自动推送版采集插件请添加官方QQ群在群文件下载

[【GitHub】](https://github.com/dayudada/ucms_caiji_python)
[【码云】](https://gitee.com/dayudada/ucms_caiji_python)

[【UCMS官方QQ讨论群】](https://jq.qq.com/?_wv=1027&k=5B9MdJp)
## 使用方法

**安装**

    pip install ucms

**项目中的引用**

    from ucms import ucms

**单文章推送函数**

    ucms.post(url,data)

成功返示例: {'code': 1, 'msg': '推送成功'}

code 状态码: 

1推送成功 

2栏目cid参数不能为空 

3栏目不存在 

4栏目某个字段不存在(msg返回信息中会说明是哪个字段) 

5采集接口网址错误 

6网络错误或其它未知错误 7网址无法访问




**多文章推送**

    ucms.post_list(url,data)

成功返回示例: {'code': 1, 'successnum': 4}

code 状态码: 1推送成功

successnum 成功推送条数

如果 成功推送条数为0 而实际推送了多条数据，说明推送失败，请用单文章推送测试错误原因

**DEMO**


    # 引用UCMS推送模块
    from ucms import ucms
    
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
