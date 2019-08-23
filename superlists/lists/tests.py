from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # 解析url，找到相应的试图函数
        found = resolve('/')
        self.assertEqual(found.func, home_page)

