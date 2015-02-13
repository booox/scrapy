#coding=utf-8


import requests
from bs4 import BeautifulSoup
import re
import os

baseURL = 'http://jandan.net/ooxx'
imageDIR = r'jpg/'
if not os.path.isdir(imageDIR):
    os.mkdir(imageDIR)


r = requests.get(baseURL)

html = r.content
# soup = BeautifulSoup(html)


pattern = r'<span class="current-comment-page">\[(\d{4})\]</span>'
match = re.search(pattern, html)
start_id = int(match.groups()[0])

for i in range(10):
    id = start_id - i
    url = r'http://jandan.net/ooxx/page-' + str(id)
    r = requests.get(url)
    html = r.content
    
    pattern = r'src="(http://ww\d{1}\.sinaimg\.cn/[^.]*\.jpg)"'
    match = re.findall(pattern, html)
    for jpg_url in match:
        print jpg_url
        
        r2 = requests.get(jpg_url)
        content = r2.content
        
        file_name = jpg_url.split('/')[-1]
        file_path = imageDIR + file_name
        with open(file_path, 'wb') as f:
            
            f.write(content)
    
    


