from config.public import Request

class  GetHandler(Request):
    """该Handler完成编号6、7、8、9协议：|/get?type=2&page=1|get|*|JSON字符串|No.142<br>带参数type=2&page=1|"""

    def get(self):
        """处理GET请求

        变量type、page存放请求中的type、page参数且二者均只包含一个值，变量args是包含着page、type变量的字典用于赋值给self.data["form"]
        """
        type = self.get_query_argument("type",default="")
        page = self.get_query_argument("page",default="")
        args = {'page': type,'type': page}
        Request.result1(self)
        self.data["args"] = args
        self.write(self.data)
