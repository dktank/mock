from config.PublicClass import Request

#|http://httpbin.org/get|get|1|JSON字符串|No.136|
class GetHandler(Request):
    def get(self):
        Request.result1(self)
        self.write(self.data)