from handlers.public import Request

class GetHandler(Request):
    '''该Handler完成编号1、2两个协议：
            |/get|get|1|JSON字符串|No.136| 和 |/get?k1=v1&k2=v2|get|2|JSON字符串|No.137<br>带参数type=1&page=1|
    '''

    def get(self):
        """处理GET请求,允许url带参数"""

        Request.result1(self)
        self.write(self.data)