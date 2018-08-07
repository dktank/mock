from config.rewrite import RequestHandler


class Status400Handler(RequestHandler):
    """该Handler完成编号13协议：|/status/400|get|response.code 400 <br>response.msg 'BAD REQUEST'|INT str|No.139<br>发起请求后的响应为response|"""

    def get(self):
        """处理GET请求

        发送400的HTTP状态码和该状态码原因：BAD REQUEST
        """
        self.send_error(status_code=400,reason="BAD REQUEST")
