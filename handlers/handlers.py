import tornado.web
class IndexHandler(tornado.web.RequestHandler):
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

class ContentHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("hello,post")

