from handlers.public import Request


class GetHandler(Request):
    '''该Handler完成编号16协议：
            |/tag/%E8%8B%B1%E5%9B%BD%20%E5%96%9C%E5%89%A7%202015|get|12||No.143 params = {'start':'20','type':'S'}|
    '''

    def get(self):
        """处理get请求,允许url带参数"""
        host = "https://movie.douban.com/"
        Request.result3(self,host)
        self.write(self.text)
