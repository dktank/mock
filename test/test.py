import unittest
import requests

class Testhttp(unittest.TestCase):
    '''单元测试类'''

    def test_get_noarg(self):
        '''测试无参数的get请求'''
        url = "http://127.0.0.1:8008/httpbin/get"
        data = {}
        text1 = Public
        text1.get(self, url, data, "args")

    def test_getarg(self):
        '''测试多个参数，一个参数含一个值的get请求'''
        url = "http://127.0.0.1:8008/httpbin/get"
        data = {"type": "1", "page": "2"}
        text1 = Public
        text1.get(self, url, data, "args")

    def test_getargs(self):
        '''测试多个参数，一个参数含多个值的get请求'''
        url = "http://127.0.0.1:8008/httpbin/get"
        data = { "k1": ["v1","v3"], "k2": "v2"}
        text1 = Public
        text1.get(self,url,data,"args")



    def test_postform(self):
        '''测试多个参数，一个参数含多个值的post请求'''
        url = "http://127.0.0.1:8008/httpbin/post"
        data = { "k1": ["v1","v3"], "k2": "v2"}
        text1 = Public
        text1.post(self,url,data,"form")

    def test_postforms(self):
        '''测试指定headers，且有多个参数，一个参数含多个值的post请求'''
        url = "http://127.0.0.1:8008/httpbin/post"
        data = {'custname':'博雅大数据学院','custtel':'010-62756975','custemail': 'service@boyabigdata.cn','delivery':'18:00','comments':'北京市海淀区北四环西路67号中关村国际创新大厦603','size':'large','topping':['mushroom','cheese']}
        headers = {'Accept': '*/*',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                 'Cache-Control': 'no-cache',
                 'Connection': 'keep-alive',
                 'Dnt': '1',
                 'Host': 'hackdata.cn',
                 'Origin': 'http://httpbin.org',
                 'Pragma': 'no-cache',
                 'Referer': 'http://httpbin.org/forms/post',
                 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'}
        reqr = requests.post(url,data=data,headers=headers)
        self.assertEqual(reqr.status_code, 200)
        data_set = reqr.json()
        for items in data:
            self.assertEqual(data_set["form"][items], data[items])
        for item in headers:
            self.assertEqual(data_set["headers"][item], headers[item])
        self.assertEqual(data_set["origin"], "192.168.1.1")

    def test_getheaders(self):
        """指定headers并验证的get请求"""
        url = "http://127.0.0.1:8008/httpbin/headers"
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                     'Accept-Encoding': 'gzip, deflate',
                     'Host': 'httpbin.org',
                     'Referer': 'http://httpbin.org',
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

        reqr = requests.get(url,headers=headers)
        self.assertEqual(reqr.status_code,200)
        data_set = reqr.json()
        print(data_set)
        for item in headers:
            self.assertEqual(data_set["headers"][item],headers[item])



class Public(unittest.TestCase):
    """公共方法类"""

    def get(self,url,data,testunit):
        """get请求公共方法"""
        reqr = requests.get(url,data)
        test_url = reqr.url
        self.assertEqual(reqr.status_code,200)
        data_set = reqr.json()
        for item in data:
            self.assertEqual(data_set[testunit][item],data[item])
        self.assertEqual(data_set["origin"],"192.168.1.1")
        self.assertEqual(data_set["url"],test_url)


    def post(self,url,data,testunit):
        """post请求公共方法"""
        reqr = requests.post(url, data)
        self.assertEqual(reqr.status_code, 200)
        test_url = reqr.url
        data_set = reqr.json()
        for item in data:
            self.assertEqual(data_set[testunit][item], data[item])
        self.assertEqual(data_set["origin"],"192.168.1.1")
        self.assertEqual(data_set["url"],test_url)

    def html(self):
        pass

if __name__=="__main__":
    unittest.main()
