#coding=utf-8

import requests
import os
import re


# get pages num
def get_pages_num(url):
    """
        return a integer for pages num
    """
    pass
    
# get proxies from a page_url
def get_proxies(page_url):
    
    pass


def main():
    
    url = 'http://www.proxy.com.ru/'
    
    pages_num = get_pages_num(url)
    
    for i in range(1, pages_num + 1):
        
        page_url = url + '/list_' + str(i) + '.html'
        proxies = get_proxies(page_url)     #  a list
        
        # write the proxies into a file
        