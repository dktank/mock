from config.RewriteRequestHandler import RequestHandler

class PostHandler(RequestHandler):
    def post(self):

        args = self.get_query_argument.__dict__
        files = dict(self.request.files) #获取上传文件列表
        header = self.request.headers #获取请求头
        appoint_header = {'Accept': '*/*',
                         'Accept-Encoding': 'gzip, deflate',
                         'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                         'Cache-Control': 'no-cache',
                         'Connection': 'keep-alive',
                         'Dnt': '1',
                         'Host': '127.0.0.1:8008',
                         'Origin': 'http://127.0.0.1:8008',
                         'Pragma': 'no-cache',
                         'Referer': 'http://httpbin.org/forms/post',
                         'Upgrade-Insecure-Requests': '1',
                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'}
        protocol = self.request.protocol #获取协议
        host = self.request.host #获取host
        uri = self.request.uri  #获取ri
        origin = protocol+'://'+host #组合origin
        url = protocol+'://'+host+uri #组合url
        try:
            lock = True
            header = dict(header)
            for key in appoint_header:
                if appoint_header[key] !=header[key]:
                    lock = False
                    break
            if lock:
                data = {u'args': args,
                         u'data': u'',
                         u'files': files,
                         u'form':   {u'comments': u'\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u5317\u56db\u73af\u897f\u8def67\u53f7\u4e2d\u5173\u6751\u56fd\u9645\u521b\u65b0\u5927\u53a6603',
                                      u'custemail': u'service@boyabigdata.cn',
                                      u'custname': u'\u535a\u96c5\u5927\u6570\u636e\u5b66\u9662',
                                      u'custtel': u'010-62756975',
                                      u'delivery': u'18:00',
                                      u'size': u'large',
                                      u'topping': [u'mushroom', u'cheese']},
                         u'headers': header,
                         u'json': None,
                         u'origin': origin,
                         u'url': url,
                }
                self.write(data)
            else:self.write("Your request header is not correct!")
        except :
            self.write_error(status_code=404)

#|http://httpbin.org/cookies/set?passport=boyabigdata|-|-|-|No.145 <br>设置cookie，带参数passport=boyabigdata|
class SetCookiesHandler(RequestHandler):
    def get(self):
        try:
            passport = self.get_argument("passport") #获取参数passport的值
            self.set_secure_cookie("passport", passport) #设置cookie
            self.write(self.get_secure_cookie("passport")) #获得cookie
        except:
            self.write("No target parameters were found")
