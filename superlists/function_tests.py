#! /home/gaofan01/develop/bin/python3
# -*- coding:utf-8 -*-
# author by Gaofan

from selenium import webdriver

browser = webdriver.Firefox()

# 伊丽丝听说有一个很酷的在线待办事项应用
# 她去看了这个应用的我首页
browser.get('http://localhost:8000')

# 她注意到网页的标题和头部都包含 “TO DO” 这个词
assert 'To-Do' in browser.title

# 应用邀请她输入一个待办事项

# 她再一个文本框中输入了 “Buy peacock feathers” （够买孔雀羽毛）
# 伊例丝的爱好是使用假蝇做鱼饵

# 她按回车键后，页面更新了
# 待办事项表格中显示了 “1: Buy peacock feathers”

# 页面中又显示了一个文本框，可以输入其他的待办事项
# 她输入了 “Use peacock feathers to make a fly”（使用孔雀羽毛做假蝇）
# 伊丽丝做事很有条理

# 伊丽丝想知道这个网站是否会记住她的清单
# 她看到网站为她生成一个唯一的URL
# 而且页面中有一些文字解说这样功能

# 她访问那个URL，发现她的待办事项列表还在

# 她很满意，去睡觉了

browser.quit()