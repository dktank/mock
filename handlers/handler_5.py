from config.public import Request

class PostHandler(Request):
    """该Handler完成编号5协议：|/post|post|5|JSON字符串|No.141<br>带参数<br>{'k2': 'v2', 'k1': ['v1', 'v3']}"""

    def post(self):
        """处理POST请求

        变量k1、k2存放请求中的k1、k2参数且k2包含一个值，k1包含多个值，变量form是包含着k1、k2变量的字典用于赋值给self.data["form"]
        """
        Request.result2(self)
        k1 = self.get_body_arguments("k")
        k2 = self.get_body_argument("k2")
        form = {"k1":k1,"k2":k2}
        self.data["form"] = form
        self.write(self.data)
