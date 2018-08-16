from config.rewrite import RequestHandler


class Status500Handler(RequestHandler):
    """该Handler完成编号22协议：|status/500|get|22|无response|No.139|"""

    def get(self):
        """处理GET请求

        设置500的HTTP状态码和该状态码原因：INTERNAL SERVER ERROR
        """

        self.set_status(status_code=500,reason="INTERNAL SERVER ERROR")
