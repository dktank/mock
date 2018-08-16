from handlers.public import Request


class PostHandler(Request):
    """该Handler完成编号3，5协议：/httpbin/post|post|3|JSON|No.137<br> body{ "k1": "v1", "k2": "v2"} |
                             和/httpbin/post|post|5|JSON|No.141<br>带参数<br>{'k2': 'v2', 'k1': ['v1', 'v3']}|
    """

    def post(self):
        """处理POST请求

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
