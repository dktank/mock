from config.RewriteRequestHandler import RequestHandler

class Request(RequestHandler):

    def result1(self):
         args = {}
         method = self.request.method
         if method != "POST":
             for key in self.request.arguments:
                if isinstance(self.get_arguments(key),list) and len(self.get_arguments(key)) == 1:
                    args[key] = self.get_argument(key)
                else:args[key] = self.get_arguments(key)
         header = dict(self.request.headers) #获取请求头
         protocol = self.request.protocol #获取协议
         host = self.request.host #获取host
         uri = self.request.uri  #获取ri
         origin = protocol+'://'+host #组合origin
         url = protocol+'://'+host+uri #组合url
         self.data = {'args': args,
                 'headers': header,
                 'origin':origin,
                 'url': url
                 }


    def result2(self):
        args = {}
        files = dict(self.request.files) #获取上传文件列表
        header = dict(self.request.headers) #获取请求头
        protocol = self.request.protocol #获取协议
        host = self.request.host #获取host
        uri = self.request.uri  #获取ri
        origin = protocol+'://'+host #组合origin
        url = protocol+'://'+host+uri #组合url
        self.data = {
                  "args": args,
                  "data": "",
                  "files": files,
                  "form": {},
                  "headers":header,
                  "json": None,
                  "origin": origin,
                  "url":url
                }




