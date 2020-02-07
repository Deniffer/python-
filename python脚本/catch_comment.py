# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:32:25 2019

@author: HASEE
"""

import requests, re, time, csv
from bs4 import BeautifulSoup as BS
from selenium import webdriver
#打开网页函数
def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    return html
#获取弹幕url中的数字id号

#当requests行不通时，采用selenium的方法。
def sele_get(url):
    SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
    driver = webdriver.PhantomJS(service_args = SERVICE_ARGS)
    driver.get(url)
    time.sleep(2)
    danmu_id = re.findall(r'cid=(\d+)&', driver.page_source)[0]

    return danmu_id


def get_danmu_id(html, url):
    try:
        soup = BS(html, 'lxml')
        #视频名
        title = soup.select('title[data-vue-meta="true"]')[0].get_text()
        #投稿人
        author = soup.select('meta[name="author"]')[0]['content']
        #弹幕的网站代码
        try:

            danmu_id = re.findall(r'cid=(\d+)&', html)[0]
            #danmu_id = re.findall(r'/(\d+)-1-64', html)[0]
            #print(danmu_id)
        except:
            danmu_id = sele_get(url)
        print(title, author)
        return danmu_id
    except:
        print('视频不见了哟')
        return False
#秒转换成时间
def sec2str(seconds):
    seconds = eval(seconds)
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    time = "%02d:%02d:%02d" % (h, m, s)
    return time

#csv保存函数
def csv_write(tablelist):
    tableheader = ['出现时间', '弹幕模式', '字号', '颜色', '发送时间' ,'弹幕池', '发送者id', 'rowID', '弹幕内容']
    with open('danmu.csv', 'w', newline='', errors='ignore') as f:
        writer = csv.writer(f)
        writer.writerow(tableheader)
        for row in tablelist:
            writer.writerow(row)


video_url ='http://www.bilibili.com/video/av5038338/'
video_html = open_url(video_url)
danmu_id = get_danmu_id(video_html, video_url)
all_list = []
if danmu_id:
    danmu_url = 'http://comment.bilibili.com/{}.xml'.format(danmu_id)
    danmu_html = open_url(url=danmu_url)
    soup = BS(danmu_html, 'lxml')
    all_d = soup.select('d')
    for d in all_d:
        #把d标签中P的各个属性分离开
        danmu_list = d['p'].split(',')
        #d.get_text()是弹幕内容
        danmu_list.append(d.get_text())
        danmu_list[0] = sec2str(danmu_list[0])
        danmu_list[4] = time.ctime(eval(danmu_list[4]))
        all_list.append(danmu_list)
        print(danmu_list)
    all_list.sort()
    csv_write(all_list)