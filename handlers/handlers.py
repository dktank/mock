import tornado.web
import urllib

#索引页"/"
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("input.html")

#No.136
class Get1Handler(tornado.web.RequestHandler):
    def get(self):
        data = {  "args": {},
                  "headers": {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
                    "Connection": "close",
                    "Cookie": "_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
                    "Host": "httpbin.org",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
                  },
                  "origin": "124.65.37.238",
                  "url": "http://httpbin.org/get"
                   }
        self.write(data)

#No.137<br>带参数type=1&page=1-get
class Get2Handler(tornado.web.RequestHandler):
    def get(self):
        k1 = self.request.arguments
        arg = {}
        for key in k1:
            arg[key] = k1[key][0].decode("utf-8")
        arg_url = urllib.parse.urlencode(arg,encoding="utf-8")
        data = {  "args": arg,
                  "headers": {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
                    "Connection": "close",
                    "Cookie": "_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
                    "Host": "httpbin.org",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
                  },
                  "origin": "124.65.37.238",
                  "url": "http://httpbin.org/get?"+arg_url
                   }
        self.write(data)

#No.137<br>带参数k1=v1&k2=v2-post
class POST1Handler(tornado.web.RequestHandler):
    def post(self):
        k1 = self.request.arguments
        arg = {}
        for key in k1:
            arg[key] = k1[key][0].decode("utf-8")
        data = {
                  "args": {},
                  "data": "",
                  "files": {},
                  "form": arg,
                  "headers": {
                    "Accept-Encoding": "identity",
                    "Connection": "close",
                    "Content-Length": "11",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "httpbin.org",
                    "User-Agent": "Python-urllib/2.7"
                  },
                  "json": "null",
                  "origin": "124.65.37.238",
                  "url": "http://httpbin.org/post"
                }
        self.write(data)

#No.137<br>带参数type=1&page=1-get
class HeadersHandler(tornado.web.RequestHandler):
    def get(self):
        header = self.request.headers #获取用户请求头
        appoint_header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                         'Accept-Encoding': 'gzip, deflate',
                         'Host': 'httpbin.org',
                         'Referer': 'http://httpbin.org',
                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
                         }
        lock = True # 验证请求头结果初始化
        header = dict(header)
        for key in appoint_header: #验证请求头
            if appoint_header[key] !=header[key]:
                lock = False
                break
        if lock: #判断请求头正确后输出结果
            data = {
                      "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "close",
                        "Host": "httpbin.org",
                        "Referer": "http://httpbin.org",
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
                      }
                    }
            self.write(data)
        else:self.write("Your request header is not correct!")

#No.139<br>发起请求后的响应为response
class Status201Handler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(status_code=201,reason="CREATED")
class Status400Handler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(status_code=400,reason="BAD REQUEST")
class Status500Handler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(status_code=500,reason="INTERNAL SERVER ERROR")

#No.141<br>带参数<br>{'k2': 'v2', 'k1': ['v1', 'v3']}
class POST2Handler(tornado.web.RequestHandler):
    def post(self):
        k1 = self.request.arguments
        print(k1)
        arg = {}
        for key in k1:
            for item in k1[key]:
                item.decode("utf-8")
            arg[key] = k1[key][0].decode("utf-8")
        data = {
                  "args": {},
                  "data": "",
                  "files": {},
                  "form": {
                    "k1": [
                      "v1",
                      "v3"
                    ],
                    "k2": "v2"
                  },
                  "headers": {
                    "Accept-Encoding": "identity",
                    "Connection": "close",
                    "Content-Length": "17",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "httpbin.org",
                    "User-Agent": "Python-urllib/2.7"
                  },
                  "json": "null",
                  "origin": "124.65.37.238",
                  "url": "http://httpbin.org/post"
                }
        self.write(data)









