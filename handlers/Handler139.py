from config.RewriteRequestHandler import RequestHandler

#|http://httpbin.org/status/201|get|response.code 201 <br>response.msg 'CREATED'|INT str|No.139<br>发起请求后的响应为response|
class Status201Handler(RequestHandler):
    def get(self):
        self.send_error(status_code=201,reason="CREATED") #设置201状态码和改状态码原因

#|http://httpbin.org/status/400|get|response.code 400 <br>response.msg 'BAD REQUEST'|INT str|No.139<br>发起请求后的响应为response||
class Status400Handler(RequestHandler):
    def get(self):
        self.send_error(status_code=400,reason="BAD REQUEST") #设置400状态码和改状态码原因

#|http://httpbin.org/status/500|get|response.code 500 <br>response.msg 'INTERNAL SERVER ERROR'|INT str|No.139<br>发起请求后的响应为response|
class Status500Handler(RequestHandler):
    def get(self):
        self.send_error(status_code=500,reason="INTERNAL SERVER ERROR") #设置500状态码和改状态码原因
