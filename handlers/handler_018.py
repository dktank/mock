from handlers.public import Request


class GetHandler(Request):
    '''该Handler完成编号17协议：|/|-|18|-|No.140 增加了cookie头：ll="108288";bid=IvJ_OIuxD_o|'''

    def get(self):
        """处理get请求,允许url带参数"""
        host = "https://www.douban.com/"
        Request.result3(self,host)
        self.set_cookie('ll',"108288")
        self.set_cookie('bid',"IvJ_OIuxD_o")
        self.write(self.text)
