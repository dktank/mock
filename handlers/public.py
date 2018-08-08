from config.rewrite import RequestHandler

class Request(RequestHandler):
    """获取的用户请求基本信息，并将他们集合成字典赋给属性data"""

    def result1(self):
         """属性data包含的信息较少，一般用域GET请求"""
         args = {}
         method = self.request.method
         if method != "POST":
             for key in self.request.arguments:
                try:
                    if isinstance(self.get_arguments(key),list) and len(self.get_arguments(key)) == 1:
                        args[key] = self.get_argument(key)
                    else:args[key] = self.get_arguments(key)
                except:
                    pass
         header = dict(self.request.headers)
         protocol = self.request.protocol
         host = self.request.host
         uri = self.request.uri
         origin = protocol+'://'+host
         url = protocol+'://'+host+uri
         self.data = {'args': args,
                 'headers': header,
                 'origin':origin,
                 'url': url
                 }


    def result2(self):
        """属性data包含的信息较多，一般用域POST请求"""
        args = {}
        files = dict(self.request.files)
        header = dict(self.request.headers)
        protocol = self.request.protocol
        host = self.request.host
        uri = self.request.uri
        origin = protocol+'://'+host
        url = protocol+'://'+host+uri
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




