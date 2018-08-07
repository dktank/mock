from config.public import Request


class PostHandler(Request):
    """该Handler完成编号3协议：|/post|post|3|JSON字符串|No.137<br>带参数k1=v1&k2=v2|"""

    def post(self):
        """处理POST请求

        变量k1、k2存放请求中的k1、k2参数且这两个参数都是包含单个值，变量form是包含着k1、k2变量的字典用于赋值给self.data["form"]
        """
        k1 = self.get_body_argument("k1")
        k2 = self.get_body_argument("k2")
        form = {"k1":k1,"k2":k2}
        Request.result2(self)
        self.data["form"] = form
        self.write(self.data)
