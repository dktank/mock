import unittest
import requests

class testhttp(unittest.TestCase):
    def setUp(self):
        self.get_url = "http://127.0.0.1:8008/get"

    #测试get请求
    def test_get(self):
        '''测试get请求的json数据'''
        resp = requests.get(self.get_url)
        data = resp.json()["1"]
        self.assertEqual(data["args"],{})
        self.assertEqual(data["headers"]["Accept"],"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
        self.assertEqual(data["headers"]["Accept-Encoding"],"gzip, deflate")
        self.assertEqual(data["headers"]["Accept-Language"],"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6")
        self.assertEqual(data["headers"]["Connection"],"close")
        self.assertEqual(data["headers"]["Cookie"],"_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1")
        self.assertEqual(data["headers"]["Host"],"httpbin.org")
        self.assertEqual(data["headers"]["Upgrade-Insecure-Requests"],"1")
        self.assertEqual(data["headers"]["User-Agent"],"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        self.assertEqual(data["origin"],"124.65.37.238")
        self.assertEqual(data["url"],"http://httpbin.org/get")



if __name__ == "__main__":
    unittest.main()