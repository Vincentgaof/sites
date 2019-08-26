#! /home/gaofan01/develop/bin/python3
# -*- coding:utf-8 -*-
# author by Gaofan

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊丽丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的我首页
        self.browser.get(self.live_server_url)

        # 她注意到网页的标题和头部都包含 “TO DO” 这个词
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #self.fail('Finish the test!')
    
        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在一个文本框输入了 “Buy peacock feathers”
        # 伊丽丝的爱好是使用假蝇做鱼饵
        inputbox.send_keys('Buy peacock feathers')

        # 她按回车键后，页面更新了
        # 待办事项表格中显示了 "1: Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        # 这里很重要休眠以下，才能查看到response
        #time.sleep(3)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了 “Use paecock feathers to make a fly”
        # 伊丽丝做事很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(3)

        # 页面再次更新，她的清单中显示了这了两个待办事项
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()
