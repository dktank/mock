from config.rewrite import RequestHandler


class Status201Handler(RequestHandler):
    """该Handler完成编号12协议：|/status/201|get|response.code 201 <br>response.msg 'CREATED'|INT str|No.139<br>发起请求后的响应为response|"""
    def get(self):
        """处理GET请求

        发送201的HTTP状态码和该状态码原因：CREATED
        """
        self.send_error(status_code=201,reason="CREATED")
