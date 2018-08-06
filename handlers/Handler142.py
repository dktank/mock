from config.RewriteRequestHandler import RequestHandler

#|http://httpbin.org/get?type=2&page=1|get|8|JSON字符串|No.142<br>带参数type=2&page=1|
class  GetHandler(RequestHandler):
    def get(self):
        try:
            header = dict(self.request.headers) #获取请求头
            type = self.get_argument("type")
            page = self.get_argument("page")
            protocol = self.request.protocol #获取协议
            host = self.request.host #获取host
            uri = self.request.uri  #获取ri
            origin = protocol+'://'+host #组合origin
            url = protocol+'://'+host+uri #组合url
            data = {'args': {'page': type,'type': page},
                    'headers': header,
                    'origin':origin,
                    'url': url}
            self.write(data)
        except:
            self.send_error(status_code=404)