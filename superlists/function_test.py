#! /home/gaofan01/develop/bin/python3
# -*- coding:utf-8 -*-
# author by Gaofan

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
