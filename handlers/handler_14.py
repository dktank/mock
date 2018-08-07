from config.rewrite import RequestHandler


class Status500Handler(RequestHandler):
    """该Handler完成编号14协议：|/status/500|get|response.code 500 <br>response.msg 'INTERNAL SERVER ERROR'|INT str|No.139<br>发起请求后的响应为response|"""

    def get(self):
        """处理GET请求

        发送500的HTTP状态码和该状态码原因：INTERNAL SERVER ERROR
        """
        self.send_error(status_code=500,reason="INTERNAL SERVER ERROR")
