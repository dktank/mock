from config.rewrite import RequestHandler

class GetHandler(RequestHandler):
    """该Handler完成编号4协议：|/httpbin/headers|get|4|JSON|No.138<br>指定请求头内容，返回请求头内容|"""

    def get(self):
        """处理GET请求"""

        header = self.request.headers
        header = dict(header)
        data = {"headers": header }
        self.write(data)