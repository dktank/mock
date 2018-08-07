from config.PublicClass import Request

class PostHandler(Request):
    def post(self):
        header = self.request.headers
        appoint_header = {'Accept': '*/*',
                         'Accept-Encoding': 'gzip, deflate',
                         'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
                         'Cache-Control': 'no-cache',
                         'Connection': 'keep-alive',
                         'Dnt': '1',
                         'Host': '127.0.0.1:8008',
                         'Origin': 'http://127.0.0.1:8008',
                         'Pragma': 'no-cache',
                         'Referer': 'http://httpbin.org/forms/post',
                         'Upgrade-Insecure-Requests': '1',
                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'}
        try:
            lock = True
            header = dict(header)
            for key in appoint_header:
                if appoint_header[key] !=header[key]:
                    lock = False
                    break
            if lock:
                Request.result2(self)
                form = {"comments" :self.get_body_argument("comments"),"custemail" :self.get_body_argument("custemail"),"custname" :self.get_body_argument("custname"),"custtel" :self.get_body_argument("custtel"),"delivery" :self.get_body_argument("delivery"),"size" :self.get_body_argument("size"),"topping" :self.get_body_arguments("topping"),}
                self.data["form"] = form
                self.write(self.data)
            else:self.write("Your request header is not correct!")
        except :
            self.write_error(status_code=404)



#|http://httpbin.org/cookies/set?passport=boyabigdata|-|-|-|No.145 <br>设置cookie，带参数passport=boyabigdata|
class SetCookiesHandler(Request):
    def get(self):
        try:
            passport = self.get_argument("passport") #获取参数passport的值
            self.set_secure_cookie("passport", passport) #设置cookie
            self.write(self.get_secure_cookie("passport")) #获得cookie
        except:
            self.write("No target parameters were found")
