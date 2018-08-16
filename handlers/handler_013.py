from handlers.public import Request

class  GetHandler(Request):
    """该Handler完成编号13,14协议：|/douban|get|13|html|No.144|
            和/|get|14|html|No.140 增加了cookie头：ll="108288";bid=IvJ_OIuxD_o|
    """

    def get(self):
        """处理GET请求"""
        self.render("doubanindex.html")