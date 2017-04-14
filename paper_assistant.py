#!/usr/bin/env python
# coding:utf-8

import requests
import urllib
from bs4 import BeautifulSoup

# 模拟header信息
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
header = {'User-Agent': user_agent}
baseUrl = 'http://xueshu.baidu.com/'
# 设置搜索关键词
keyword = 'magnetic reconnection'
data = {'wd': keyword, 'tn': 'SE_baiduxueshu_c1gjeupa', 'ie': 'utf-8'}
data = urllib.urlencode(data)
url = baseUrl + 's?' + data
# 构建请求的request
request = requests.get(url, headers=header)
data = request.text
# 将信息传入bs4
soup = BeautifulSoup(data, 'html.parser')

#print soup.body.div.find_all('div',id = 'leftnav',class_='xpath-log')
#print soup.body.div.div.div.div.div.contents
# 得到有效信息的网页
filter_url = soup.body.div.find('div',id = 'leftnav',class_='xpath-log')

# 生成信息收集的空列表
fecthed_data_add_all = []
for item in filter_url:
    useful_url = item.div.div
    #print useful_url
    #print 'fenge'
    #url_list = useful_url.find_all('a',class_ = 'OP_LOG_BTN sc_nav_tag left_list_short_show')
    url_list = useful_url.find_all('a')
    #print url_list
    if not url_list==[]:    #不为空
        for l in url_list:
            #print l
            i = l.get('title')
            j = l.get('data-num')
            fecthed_data_add_all.append(i)
            fecthed_data_add_all.append(j)
        #fecthed_data_add_all.append(lambda:l.get('title') for l in url_list)
        #fecthed_data_add_all.append(lambda: l.get('data-num') for l in url_list)


#将文件写入list.txt文档
file_data = open('list.txt','w')
#file_data.writelines(fecthed_data_add_all)
for i in fecthed_data_add_all:
    if i:
        #print i
        try:
            file_data.write(i)
            file_data.write('\n')
        except UnicodeEncodeError:
            pass
file_data.close()

