from config.RewriteRequestHandler import RequestHandler

#|http://httpbin.org/get|get|1|JSON字符串|No.136|
class GetHandler(RequestHandler):
    def get(self):
        protocol = self.request.protocol #获取协议
        host = self.request.host #获取host
        uri = self.request.uri  #获取ri
        args = self.get_query_argument.__dict__
        headers = dict(self.request.headers) #获取请求头
        origin = protocol+'://'+host #组合origin
        url = protocol+'://'+host+uri #组合url
        data = {  "args": args,
                  "headers":headers ,
                  "origin": origin,
                  "url": url
                   }
        self.write(data)
