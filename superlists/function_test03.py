#! /home/gaofan01/develop/bin/python3
# -*- coding:utf-8 -*-
# author by Gaofan

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 伊丽丝听说有一个很酷的在线待办事项应用
        # 她去看了这个应用的我首页
        self.browser.get('http://localhost:8000')

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
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # 页面中又显示了一个文本框，可以输入其他的待办事项
        # 她输入了 “Use paecock feathers to make a fly”
        # 伊丽丝做事很有条理
        self.fail('Finish the test')

if __name__ == '__main__':
    unittest.main()
