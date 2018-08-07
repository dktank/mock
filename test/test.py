import unittest
import requests

class Equal(unittest.TestCase):
    def equal_fun(self,data,target_data):
        for item in data:
            try:
                if len(data[item])==0:
                    self.assertEqual(data[item],target_data[item])
                else:
                    if type(data[item]) is not dict:
                        if type(data[item]) is  list:
                            len_num = len(data[item])
                            for i in range(len_num):
                                self.assertEqual(data[item][i],target_data[item][i])
                        else:
                            self.assertEqual(data[item],target_data[item])
                    else:Equal.equal_fun(self,data[item],target_data[item])
            except:
                self.assertEqual(data[item],target_data[item])

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
    # def test_get(self):
    #     '''测试No.137带参数type=1&page=1-get'''
    #     get_url = "http://127.0.0.1:8008/get?type=1&page=1"
    #     reqr = requests.get(get_url)
    #     self.assertEqual(reqr.status_code,200)
    #     data = reqr.json()
    #     self.assertEqual(data["args"],{"type":"1","page":"1"})
    #     self.assertEqual(data["headers"]["Accept"],"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8")
    #     self.assertEqual(data["headers"]["Accept-Encoding"],"gzip, deflate")
    #     self.assertEqual(data["headers"]["Accept-Language"],"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6")
    #     self.assertEqual(data["headers"]["Connection"],"close")
    #     self.assertEqual(data["headers"]["Cookie"],"_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1")
    #     self.assertEqual(data["headers"]["Host"],"httpbin.org")
    #     self.assertEqual(data["headers"]["Upgrade-Insecure-Requests"],"1")
    #     self.assertEqual(data["headers"]["User-Agent"],"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36")
    #     self.assertEqual(data["origin"],"124.65.37.238")
    #     self.assertEqual(data["url"],"http://httpbin.org/get?type=1&page=1")

    #测试No.137带参数k1=v1&k2=v2-post
    # def test_post(self):
    #     '''测试No.137带参数k1=v1&k2=v2-post'''
    #     self.get_url = "http://127.0.0.1:8008/post"
    #     reqr = requests.post(self.get_url,{"k1":"1","k2":"2"})
    #     self.assertEqual(reqr.status_code,200)
    #     data = reqr.json()
    #     self.assertEqual(data["args"],{})
    #     self.assertEqual(data["data"],"")
    #     self.assertEqual(data["files"],{})
    #     self.assertEqual(data["form"],{"k1": "1","k2": "2"})
    #     self.assertEqual(data["headers"]["Accept-Encoding"],"identity")
    #     self.assertEqual(data["headers"]["Connection"],"close")
    #     self.assertEqual(data["headers"]["Content-Length"],"11")
    #     self.assertEqual(data["headers"]["Content-Type"],"application/x-www-form-urlencoded")
    #     self.assertEqual(data["headers"]["Host"],"httpbin.org")
    #     self.assertEqual(data["headers"]["User-Agent"],"Python-urllib/2.7")
    #     self.assertEqual(data["json"],"null")
    #     self.assertEqual(data["origin"],"124.65.37.238")
    #     self.assertEqual(data["url"],"http://httpbin.org/post")

    #测试No.138指定请求头内容，然后发起请求  正确请求头
    def test_headers(self):
        '''测试No.138指定请求头内容，然后发起请求  正确请求头'''
        get_url = "http://127.0.0.1:8008/headers"
        headr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-Encoding': 'gzip, deflate',
                 'Host': 'httpbin.org',
                 'Referer': 'http://httpbin.org',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
        reqr = requests.get(get_url,headers = headr)
        self.assertEqual(reqr.status_code,200)
        header = {'headers':reqr.request.headers}
        data = reqr.json()
        equa = Equal
        equa.equal_fun(self,data,header)
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

    #No.141<br>带参数<br>{'k2': 'v2', 'k1': ['v1', 'v3']}
    # def test_post(self):
    #     '''测试No.141带参数{'k2': 'v2', 'k1': ['v1', 'v3']}'''
    #     self.get_url = "http://127.0.0.1:8008/post"
    #     reqr = requests.post(self.get_url,{'k2': 'v2', 'k1': ['v1', 'v3']})
    #     self.assertEqual(reqr.status_code,200)
    #     data = reqr.json()
    #     self.assertEqual(data["args"],{})
    #     self.assertEqual(data["data"],"")
    #     self.assertEqual(data["files"],{})
    #     self.assertEqual(data["form"],{"k1": ["v1", "v3"], "k2": "v2" })
    #     self.assertEqual(data["headers"]["Accept-Encoding"],"identity")
    #     self.assertEqual(data["headers"]["Connection"],"close")
    #     self.assertEqual(data["headers"]["Content-Length"],"17")
    #     self.assertEqual(data["headers"]["Content-Type"],"application/x-www-form-urlencoded")
    #     self.assertEqual(data["headers"]["Host"],"httpbin.org")
    #     self.assertEqual(data["headers"]["User-Agent"],"Python-urllib/2.7")
    #     self.assertEqual(data["json"],"null")
    #     self.assertEqual(data["origin"],"124.65.37.238")
    #     self.assertEqual(data["url"],"http://httpbin.org/post")
     #No.142<br>带参数type=1&page=1
    # def test_get(self):
    #     '''测试No.142带参数type=1&page=1'''
    #     def testarg_200(args):
    #         get_url = "http://127.0.0.1:8008/get"
    #         reqr = requests.get(get_url,data = args)
    #         self.assertEqual(reqr.status_code,200)
    #         data = reqr.json()
    #         self.assertEqual(data["args"],{'page': args["type"], 'type': args["page"]})
    #         self.assertEqual(data["headers"]["Accept-Encoding"],"identity")
    #         self.assertEqual(data["headers"]["Connection"],"close")
    #         self.assertEqual(data["headers"]["Host"],"httpbin.org")
    #         self.assertEqual(data["headers"]["User-Agent"],"Python-urllib/2.7")
    #         self.assertEqual(data["origin"],"124.65.37.238")
    #         self.assertEqual(data["url"],"http://httpbin.org/get?type=1&page=1")
    #     def testarg_404(args):
    #         get_url = "http://127.0.0.1:8008/get"
    #         reqr = requests.get(get_url,data = args)
    #         self.assertEqual(reqr.status_code,404)
    #     testarg_200({'type': '1', 'page': '1'})
    #     testarg_200({'type': '1', 'page': '2'})
    #     testarg_200({'type': '2', 'page': '1'})
    #     testarg_200({'type': '2', 'page': '2'})
    #     testarg_404({'error': '2', 'page': '2'})

    def test_post145(self):
        '''测试No.145指定请求头内容，然后发起请求'''
        get_url = "http://127.0.0.1:8008/post"
        headr = {'Accept': '*/*',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                 'Cache-Control': 'no-cache',
                 'Connection': 'keep-alive',
                 'Dnt': '1',
                 'Host': r'127.0.0.1:8008',
                 'Origin': r'http://127.0.0.1:8008',
                 'Pragma': 'no-cache',
                 'Referer': 'http://httpbin.org/forms/post',
                 'Upgrade-Insecure-Requests': '1',
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'}
        data1 = {u'comments': u'\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u5317\u56db\u73af\u897f\u8def67\u53f7\u4e2d\u5173\u6751\u56fd\u9645\u521b\u65b0\u5927\u53a6603',
                      u'custemail': u'service@boyabigdata.cn',
                      u'custname': u'\u535a\u96c5\u5927\u6570\u636e\u5b66\u9662',
                      u'custtel': u'010-62756975',
                      u'delivery': u'18:00',
                      u'size': u'large',
                      u'topping': [u'mushroom', u'cheese']}
        reqr = requests.post(get_url,data = data1,headers = headr)
        header = reqr.request.headers
        url = reqr.request.url
        origin = header['Origin']
        self.assertEqual(reqr.status_code,200)
        data = reqr.json()
        target_data = {u'args': {},
                     u'data': u'',
                     u'files': {},
                     u'form': {u'comments': u'\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u5317\u56db\u73af\u897f\u8def67\u53f7\u4e2d\u5173\u6751\u56fd\u9645\u521b\u65b0\u5927\u53a6603',
                      u'custemail': u'service@boyabigdata.cn',
                      u'custname': u'\u535a\u96c5\u5927\u6570\u636e\u5b66\u9662',
                      u'custtel': u'010-62756975',
                      u'delivery': u'18:00',
                      u'size': u'large',
                      u'topping': [u'mushroom', u'cheese']},
                     u'headers': header,
                     u'json': None,
                     u'origin':  origin,
                     u'url':url}
        equa = Equal
        equa.equal_fun(self,data,target_data)



    def test_get149(self):
        '''测试No.149带参数{'name':'张三', 'hobbies': ['篮球','足球','羽毛球'], 'transcripts':{'语文':30, '数学': 99.5}}'''
        get_url = "http://127.0.0.1:8008/get"
        data = {u'profile': u'{"transcripts": {"\\u6570\\u5b66": 99.5, "\\u8bed\\u6587": 30}, "name": "\\u5f20\\u4e09", "hobbies": ["\\u7bee\\u7403", "\\u8db3\\u7403", "\\u7fbd\\u6bdb\\u7403"]}'}
        reqr = requests.get(get_url,params = data)
        header = reqr.request.headers
        url = reqr.request.url
        header["Host"] = "127.0.0.1:8008"
        target_data = {u'args': data,
                         u'headers': header,
                         u'origin': u'http://127.0.0.1:8008',
                         u'url': url}
        self.assertEqual(reqr.status_code,200)
        datas = reqr.json()
        equa = Equal
        equa.equal_fun(self,target_data,datas)

if __name__ == "__main__":
    unittest.main()