from config.PublicClass import Request

#|http://httpbin.org/get?k1=v1&k2=v2|get|2|JSON字符串|No.137<br>带参数type=1&page=1|
class GetHandler(Request):
    def get(self):
        Request.result1(self)
        self.write(self.data)
