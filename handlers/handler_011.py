from handlers.public import Request

class  GetHandler(Request):
    """该Handler完成编号11协议：|/get|get|11|JSON字符串
       |No.149|带参数{'name':'张三', 'hobbies': ['篮球','足球','羽毛球'], 'transcripts':{'语文':30, '数学': 99.5}}
    """

    def get(self):
        """处理GET请求

        变量profile存放请求中的profile参数值，变量args是包含着profile变量的字典用于赋值给self.data["form"]
        """
        try:
            Request.result1(self)
            profile = self.get_query_argument("profile")
            args = {'profile':profile}
            self.data["args"] = args
            self.write(self.data)
        except:
            self.send_error(status_code=404)
