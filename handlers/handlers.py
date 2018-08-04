import tornado.web
import urllib

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("input.html")

class Get136Handler(tornado.web.RequestHandler):
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

class Get137Handler(tornado.web.RequestHandler):
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


class POST137Handler(tornado.web.RequestHandler):
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


class Headers137Handler(tornado.web.RequestHandler):
    def get(self):
        header = self.request.headers
        appoint_header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                         'Accept-Encoding': 'gzip, deflate',
                         'Host': 'httpbin.org',
                         'Referer': 'http://httpbin.org',
                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
                         }
        lock = True
        header = dict(header)
        for key in appoint_header:
            if appoint_header[key] !=header[key]:
                lock = False
                break
        if lock:
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

class Status201Handler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(status_code=201,reason="CREATED")
class Status400Handler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(status_code=400,reason="BAD REQUEST")
class Status500Handler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(status_code=500,reason="INTERNAL SERVER ERROR")

class POST141Handler(tornado.web.RequestHandler):
    def post(self):
        k1 = self.get_arguments("k1")
        k2 = self.get_argument("k2")
        form = {"k1":k1,"k2":k2}
        data = {
                  "args": {},
                  "data": "",
                  "files": {},
                  "form": form,
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

class  Get142Handler(tornado.web.RequestHandler):
    def get(self):
        try:
            type = self.get_argument("type")
            page = self.get_argument("page")
            data = {'args': {'page': type,'type': page},
                    'headers': {'Accept-Encoding': 'identity',
                    'Connection': 'close',
                    'Host': 'httpbin.org',
                    'User-Agent': 'Python-urllib/2.7'},
                    'origin': '124.65.37.238',
                    'url': 'http://httpbin.org/get?type=1&page=1'}
            self.write(data)
        except:
            self.send_error(status_code=404)
class POST145Handler(tornado.web.RequestHandler):
    def post(self):
        header = self.request.headers
        appoint_header = {'Accept': '*/*',
                         'Accept-Encoding': 'gzip, deflate',
                         'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                         'Cache-Control': 'no-cache',
                         'Connection': 'keep-alive',
                         'Dnt': '1',
                         'Host': 'httpbin.org',
                         'Origin': 'http://httpbin.org',
                         'Pragma': 'no-cache',
                         'Referer': 'http://httpbin.org/forms/post',
                         'Upgrade-Insecure-Requests': '1',
                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'}
        try:
            lock = True
            header = dict(header)
            for key in appoint_header:
                if appoint_header[key] !=header[key]:
                    lock = False
                    break
            if lock:
                data = {u'args': {},
                         u'data': u'',
                         u'files': {},
                         u'form': {u'comments': u'\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u5317\u56db\u73af\u897f\u8def67\u53f7\u4e2d\u5173\u6751\u56fd\u9645\u521b\u65b0\u5927\u53a6603',
                          u'custemail': u'service@boyabigdata.cn',
                          u'custname': u'\u535a\u96c5\u5927\u6570\u636e\u5b66\u9662',
                          u'custtel': u'010-62756975',
                          u'delivery': u'18:00',
                          u'size': u'large',
                          u'topping': [u'mushroom', u'cheese']},
                         u'headers': {u'Accept': u'*/*',
                          u'Accept-Encoding': u'gzip, deflate',
                          u'Accept-Language': u'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                          u'Cache-Control': u'no-cache',
                          u'Connection': u'close',
                          u'Content-Length': u'392',
                          u'Content-Type': u'application/x-www-form-urlencoded',
                          u'Cookie': u'passport=boyabigdata',
                          u'Dnt': u'1',
                          u'Host': u'httpbin.org',
                          u'Origin': u'http://httpbin.org',
                          u'Pragma': u'no-cache',
                          u'Referer': u'http://httpbin.org/forms/post',
                          u'Upgrade-Insecure-Requests': u'1',
                          u'User-Agent': u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'},
                         u'json': None,
                         u'origin': u'124.65.37.238',
                         u'url': u'http://httpbin.org/post'}
                self.write(data)
            else:self.write("Your request header is not correct!")
        except :
            self.write_error(status_code=404)

class Cookies_setHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            passport = self.get_argument("passport")
            self.set_secure_cookie("passport", passport)
            self.write(self.get_secure_cookie("passport"))

        except:
            self.write("No target parameters were found")

class  Get149Handler(tornado.web.RequestHandler):
    def get(self):
        try:
            name = self.get_argument("name")
            hobbies = self.get_arguments("hobbies")
            transcripts = self.get_arguments("transcripts")
            data = {u'args': {u'profile': u'{"transcripts": {"\\u6570\\u5b66": 99.5, "\\u8bed\\u6587": 30}, "name": "\\u5f20\\u4e09", "hobbies": ["\\u7bee\\u7403", "\\u8db3\\u7403", "\\u7fbd\\u6bdb\\u7403"]}'},
                     u'headers': {u'Accept': u'*/*',
                      u'Accept-Encoding': u'gzip, deflate',
                      u'Connection': u'close',
                      u'Host': u'httpbin.org',
                      u'User-Agent': u'python-requests/2.18.4'},
                     u'origin': u'124.65.37.238',
                     u'url': u'http://httpbin.org/get?profile={"transcripts"%3A+{"\\u6570\\u5b66"%3A+99.5%2C+"\\u8bed\\u6587"%3A+30}%2C+"name"%3A+"\\u5f20\\u4e09"%2C+"hobbies"%3A+["\\u7bee\\u7403"%2C+"\\u8db3\\u7403"%2C+"\\u7fbd\\u6bdb\\u7403"]}'}
            self.write(data)
        except:
            self.send_error(status_code=404)









