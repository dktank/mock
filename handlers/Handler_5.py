from config.PublicClass import Request

#|http://httpbin.org/post|post|5|JSON字符串|No.141<br>带参数<br>{'k2': 'v2', 'k1': ['v1', 'v3']}|
class PostHandler(Request):
    def post(self):
        Request.result2(self)
        k1 = self.get_body_arguments("k1")
        k2 = self.get_body_argument("k2")
        form = {"k1":k1,"k2":k2}
        self.data["form"] = form
        self.write(self.data)
