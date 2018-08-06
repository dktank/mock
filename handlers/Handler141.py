from config.RewriteRequestHandler import RequestHandler

#|http://httpbin.org/post|post|5|JSON字符串|No.141<br>带参数<br>{'k2': 'v2', 'k1': ['v1', 'v3']}|
class PostHandler(RequestHandler):
    def post(self):
        args = self.get_query_argument.__dict__
        files = dict(self.request.files) #获取上传文件列表
        header = dict(self.request.headers) #获取请求头
        k1 = self.get_body_argument("k1")
        k2 = self.get_body_argument("k2")
        form = {"k1":k1,"k2":k2}
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
                  "headers": header,
                  "json": None,
                  "origin": origin,
                  "url": url
                }
        self.write(data)
