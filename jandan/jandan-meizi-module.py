#coding=utf-8

import requests
import os
import re

def get_html(url):
    # proxy = {"http": "http://207.91.10.234:8080"}   # high-anonymous
    proxy = {"http":"http://193.232.184.141:8080"}
    headers = {
        "User-Agent":'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36',
    }
    
    r = requests.get(url)
    html = r.content
    
    return html

def get_page_num(url):
    
    html = get_html(url)
    
    pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>'
    match = re.search(pattern, html)
    page_num = int(match.groups()[0])
    # print page_num
    return page_num

    

def get_page_jpgs(page_url):
    jpg_adds_list = []
    
    html = get_html(page_url)
    
    pattern = r'src="(http://ww\d{1}\.sinaimg\.cn/[^.]*\.jpg)"'
    match = re.findall(pattern, html)
    
    for jpg_url in match:
        jpg_adds_list.append(jpg_url)
        # print jpg_url
    return jpg_adds_list
    
def save_jpgs(jpg_adds_list):
    
    for jpg_url in jpg_adds_list:
        html = get_html(jpg_url)
        
        file_name = jpg_url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(html)
        print jpg_url

def download_mz():
    url = r'http://jandan.net/ooxx'
    dir = 'ooxx/'
    if not os.path.isdir(dir):
        os.mkdir(dir)
    os.chdir(dir)
    
    page_num = get_page_num(url)
    
    for i in range(13, 14):
        page_id = page_num - i
        page_url = url + '/page-' + str(page_id)
        print page_url
        print '-' * 30
        jpg_adds_list = get_page_jpgs(page_url)
        save_jpgs(jpg_adds_list)

if __name__ == '__main__':
    download_mz()