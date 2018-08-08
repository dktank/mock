from handlers.public import Request

class PostHandler(Request):
    """该Handler完成编号10协议：|/post|post|10|JSON字符串|No.145<br>指定请求头内容，然后发起请求|"""

    def post(self):
        """处理POST请求,验证headers

        变量header存放用户的请求头，lock存放验证请求头结果的变量初始化为真
        字典form存放请求参数信息，赋值给self.data["form"]并将其作为响应数据输出
        """
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
