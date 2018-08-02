import unittest
import requests

class testhttp(unittest.TestCase):

    #测试No.136
    # def test_get(self):
    #     '''测试No.136'''
    #     get_url = "http://127.0.0.1:8008/get"
    #     reqr = requests.get(get_url)
    #     data = reqr.json()
    #     self.assertEqual(data["args"],{})
    #     self.assertEqual(data["headers"]["Accept"],"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
    #     self.assertEqual(data["headers"]["Accept-Encoding"],"gzip, deflate")
    #     self.assertEqual(data["headers"]["Accept-Language"],"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6")
    #     self.assertEqual(data["headers"]["Connection"],"close")
    #     self.assertEqual(data["headers"]["Cookie"],"_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1")
    #     self.assertEqual(data["headers"]["Host"],"httpbin.org")
    #     self.assertEqual(data["headers"]["Upgrade-Insecure-Requests"],"1")
    #     self.assertEqual(data["headers"]["User-Agent"],"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    #     self.assertEqual(data["origin"],"124.65.37.238")
    #     self.assertEqual(data["url"],"http://httpbin.org/get")

    #测试No.137<br>带参数type=1&page=1-get
    def test_get(self):
        '''测试No.137带参数type=1&page=1-get'''
        get_url = "http://127.0.0.1:8008/get?type=1&page=1"
        reqr = requests.get(get_url)
        self.assertEqual(reqr.status_code,200)
        data = reqr.json()
        self.assertEqual(data["args"],{"type":"1","page":"1"})
        self.assertEqual(data["headers"]["Accept"],"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
        self.assertEqual(data["headers"]["Accept-Encoding"],"gzip, deflate")
        self.assertEqual(data["headers"]["Accept-Language"],"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6")
        self.assertEqual(data["headers"]["Connection"],"close")
        self.assertEqual(data["headers"]["Cookie"],"_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1")
        self.assertEqual(data["headers"]["Host"],"httpbin.org")
        self.assertEqual(data["headers"]["Upgrade-Insecure-Requests"],"1")
        self.assertEqual(data["headers"]["User-Agent"],"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
        self.assertEqual(data["origin"],"124.65.37.238")
        self.assertEqual(data["url"],"http://httpbin.org/get?type=1&page=1")

    #测试No.137带参数k1=v1&k2=v2-post
    def test_post(self):
        '''测试No.137带参数k1=v1&k2=v2-post'''
        self.get_url = "http://127.0.0.1:8008/post"
        reqr = requests.post(self.get_url,{"k1":"1","k2":"2"})
        self.assertEqual(reqr.status_code,200)
        data = reqr.json()
        self.assertEqual(data["args"],{})
        self.assertEqual(data["data"],"")
        self.assertEqual(data["files"],{})
        self.assertEqual(data["form"],{"k1": "1","k2": "2"})
        self.assertEqual(data["headers"]["Accept-Encoding"],"identity")
        self.assertEqual(data["headers"]["Connection"],"close")
        self.assertEqual(data["headers"]["Content-Length"],"11")
        self.assertEqual(data["headers"]["Content-Type"],"application/x-www-form-urlencoded")
        self.assertEqual(data["headers"]["Host"],"httpbin.org")
        self.assertEqual(data["headers"]["User-Agent"],"Python-urllib/2.7")
        self.assertEqual(data["json"],"null")
        self.assertEqual(data["origin"],"124.65.37.238")
        self.assertEqual(data["url"],"http://httpbin.org/post")

    #测试No.138指定请求头内容，然后发起请求  正确请求头
    def test_headers(self):
        '''测试No.138指定请求头内容，然后发起请求  正确请求头'''
        get_url = "http://127.0.0.1:8008/headers"
        headr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-encoding': 'gzip, deflate',
                 'Host': 'httpbin.org',
                 'Referer': 'http://httpbin.org',
                 'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        reqr = requests.get(get_url,headers = headr)
        self.assertEqual(reqr.status_code,200)
        data = reqr.json()
        self.assertEqual(data["headers"]["Accept-Encoding"],"gzip, deflate")
        self.assertEqual(data["headers"]["Connection"],"close")
        self.assertEqual(data["headers"]["Accept"],"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        self.assertEqual(data["headers"]["Referer"],"http://httpbin.org")
        self.assertEqual(data["headers"]["Host"],"httpbin.org")
        self.assertEqual(data["headers"]["User-Agent"],"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36")

    #测试No.138指定请求头内容，然后发起请求  错误请求头
    def test_errorheaders(self):
        '''测试No.138指定请求头内容，然后发起请求  错误请求头'''
        get_url = "http://127.0.0.1:8008/headers"
        headr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.9',
                 'Accept-encoding': 'gzip, deflate',
                 'Host': 'httpbin.org',
                 'Referer': 'http://httpbin.org',
                 'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        reqr = requests.get(get_url,headers = headr)
        self.assertEqual(reqr.status_code,200)
        self.assertEqual(reqr.content.decode("utf-8"),"Your request header is not correct!")

    #测试No.139<br>发起请求后的响应为response
    def test_status201(self):
        '''验证状态码201'''
        get_url = "http://127.0.0.1:8008/status/201"
        reqr = requests.get(get_url)
        self.assertEqual(reqr.status_code,201)
        self.assertEqual(reqr.reason,'CREATED')
    def test_status400(self):
        '''验证状态码400'''
        get_url = "http://127.0.0.1:8008/status/400"
        reqr = requests.get(get_url)
        self.assertEqual(reqr.status_code,400)
        self.assertEqual(reqr.reason,'BAD REQUEST')
    def test_status500(self):
        '''验证状态码500'''
        get_url = "http://127.0.0.1:8008/status/500"
        reqr = requests.get(get_url)
        self.assertEqual(reqr.status_code,500)
        self.assertEqual(reqr.reason,'INTERNAL SERVER ERROR')


if __name__ == "__main__":
    unittest.main()