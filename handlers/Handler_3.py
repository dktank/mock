from config.PublicClass import Request

#|http://httpbin.org/post|post|3|JSON字符串|No.137<br>带参数k1=v1&k2=v2|
class PostHandler(Request):
    def post(self):
        k1 = self.get_body_argument("k1") #获得参数k1值
        k2 = self.get_body_argument("k2") #获得参数k2值
        form = {"k1":k1,"k2":k2} #组合成字典
        Request.result2(self)
        self.data["form"] = form
        self.write(self.data)
