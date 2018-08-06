from config.RewriteRequestHandler import RequestHandler
import json
#|http://httpbin.org/get?k1=v1&k2=v2|get|2|JSON字符串|No.137<br>带参数type=1&page=1|
class GetHandler(RequestHandler):
    def get(self):
        args = self.get_query_argument.__dict__
        print(args)
        header = dict(self.request.headers) #获取请求头
        protocol = self.request.protocol #获取协议
        host = self.request.host #获取host
        uri = self.request.uri  #获取ri
        origin = protocol+'://'+host #组合origin
        url = protocol+'://'+host+uri #组合url
        data = {  "args": args,
                  "headers": header,
                  "origin": origin,
                  "url": url
                   }
        self.write(data)

#|http://httpbin.org/post|post|3|JSON字符串|No.137<br>带参数k1=v1&k2=v2|
class PostHandler(RequestHandler):
    def post(self):
        args = self.get_query_argument.__dict__
        files = dict(self.request.files) #获取上传文件列表
        header = dict(self.request.headers) #获取请求头
        k1 = self.get_body_argument("k1") #获得参数k1值
        k2 = self.get_body_argument("k2") #获得参数k2值
        form = {"k1":k1,"k2":k2} #组合成字典
        protocol = self.request.protocol #获取协议
        host = self.request.host #获取host
        uri = self.request.uri  #获取ri
        origin = protocol+'://'+host #组合origin
        url = protocol+'://'+host+uri #组合url
        data = {
                  "args": args,
                  "data": "",
                  "files": files,
                  "form": form,
                  "headers":header,
                  "json": None,
                  "origin": origin,
                  "url":url
                }
        self.write(data)
