from handlers.public import Request


class PostHandler(Request):
    """该Handler完成编号3协议：|/post|post|3|JSON字符串|No.137<br>带参数k1=v1&k2=v2|"""

    def post(self):
        """处理POST请求

        变量k1、k2存放请求中的k1、k2参数且这两个参数都是包含单个值，
        变量form是包含着k1、k2变量的字典用于赋值给self.data["form"]
        """
        data = {
              "args": {},
              "data": "",
              "files": {},
              "form": {
                "k1": "v1",
                "k2": "v23"
              },
              "headers": {
                "Accept-Encoding": "identity",
                "Connection": "close",
                "Content-Length": "11",
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "httpbin.org",
                "User-Agent": "Python-urllib/2.7"
              },
              "json": None,
              "origin": "124.65.37.238",
              "url": "http://httpbin.org/post"
              }
        res_data = Request.post_result1(self,data)
        self.write(res_data)
