from config.RewriteRequestHandler import RequestHandler

#|http://httpbin.org/get|get|11|JSON字符串|No.149|
#带参数{'name':'张三', 'hobbies': ['篮球','足球','羽毛球'], 'transcripts':{'语文':30, '数学': 99.5}}

class  GetHandler(RequestHandler):
    def get(self):
        try:
            name = self.get_argument("name") #获取参数name的值
            hobbies = self.get_arguments("hobbies") #获取参数hobbies的值
            transcripts = self.get_arguments("transcripts") #获取参数transcripts的值
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
