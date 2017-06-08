# coding:utf-8

from bs4 import BeautifulSoup
import requests
from urllib import urlretrieve
import os
import threading

numMutex = threading.Lock()
g_threadNum = 0

def downloadImg(url):
    html = requests.get(url)
    bsObj = BeautifulSoup(html.text, 'html.parser')
    if not os.path.exists('jiandan/'):
        os.mkdir('jiandan/')
    for i in bsObj.findAll('img'):
        if i['src'].startswith('//wx'):
            #下载远程数据
            print '%s is downloading.....' % i['src'].split('/')[-1]
            urlretrieve('http:' + i['src'], 'jiandan/' + i['src'].split('/')[-1])
            print 'completed!'
    print 'The images download completed!'

class MyThread(threading.Thread):
    def __init__(self, url):
        self.url = url
        threading.Thread.__init__(self)

    def run(self):
        numMutex.acquire()
        downloadImg(self.url)
        global g_threadNum
        g_threadNum -= 1
        numMutex.release()

def webspider():
    start = int(raw_input('请输入开始页数：'))
    end = int(raw_input('请输入结束页数：'))
    urlPool = ["http://jandan.net/ooxx/page-{}#comments".format(str(i)) for i in range(start, end)]
    global g_threadNum
    threadLimit = 5  #使用5个线程
    while urlPool != []:
        if g_threadNum < threadLimit:
            newUrl = urlPool.pop()
            g_threadNum += 1
            newThread = MyThread(newUrl)
            newThread.start()

if __name__ == '__main__':
    webspider()
