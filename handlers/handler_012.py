from handlers.public import Request

class  GetHandler(Request):
    """该Handler完成编号12协议：|/douban/tag/%E8%8B%B1%E5%9B%BD%20%E5%96%9C%E5%89%A7%202015|get|12|html|No.143 带参数
        {'start':'20','type':'S'}|
    """

    def get(self):
        """处理GET请求"""
        self.render("英国 喜剧 2015.html")

