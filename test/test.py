import unittest
from tornado.testing import AsyncHTTPTestCase
from App import application

class testhttp(AsyncHTTPTestCase):
    def get_app(self):
        return application.application

    #测试get请求
    def test_get(self):
        response = self.fetch('/get')
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'hello,get')

    #测试post请求
    def test_post(self):
        body = ''
        response = self.fetch('/post',method='POST',body=body)
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'hello,post')

if __name__ == "__main__":
    unittest.main()