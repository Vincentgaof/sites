from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # 解析url，找到相应的试图函数
        found = resolve('/')
        self.assertEqual(found.func, home_page)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_view_return_correct_html(self):
        # 用户在浏览器请求时，django看到的就是request对象
        request = HttpRequest()
        # 把request对象传递给试图函数
        response = home_page(request)

        # 提取响应中的content，并且把原始字节转换诚html字符串
        html = response.content.decode('utf-8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

