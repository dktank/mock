from handlers.public import Request


class GetHandler(Request):
    '''该Handler完成编号17协议：|/|-|17|-|No.140|
    '''

    def get(self):
        """处理get请求,允许url带参数"""
        host = "https://www.douban.com/"
        Request.result3(self,host)
        self.write(self.text)
