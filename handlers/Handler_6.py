from config.PublicClass import Request

#|http://httpbin.org/get?type=2&page=1|get|8|JSON字符串|No.142<br>带参数type=2&page=1|
class  GetHandler(Request):
    def get(self):
        type = self.get_argument("type")
        page = self.get_argument("page")
        Request.result1(self)
        self.data["args"] = {'page': type,'type': page}
        self.write(self.data)
