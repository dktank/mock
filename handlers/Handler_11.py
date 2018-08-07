from config.PublicClass import Request

#|http://httpbin.org/get|get|11|JSON字符串|No.149|
#带参数{'name':'张三', 'hobbies': ['篮球','足球','羽毛球'], 'transcripts':{'语文':30, '数学': 99.5}}

class  GetHandler(Request):
    def get(self):
        try:
            Request.result1(self)
            profile = self.get_query_argument("profile")#获取参数profile的值
            args = {'profile':profile}
            self.data["args"] = args
            self.data["headers"]["Host"] = self.request.host
            self.write(self.data)
        except:
            self.send_error(status_code=404)
