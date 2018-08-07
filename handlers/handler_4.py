from config.rewrite import RequestHandler

class GetHandler(RequestHandler):
    """该Handler完成编号4协议：|/headers|get|4|JSON字符串|No.138<br>指定请求头内容，然后发起请求|"""

    def get(self):
        """处理GET请求,验证headers

        变量header存放用户的请求头，lock存放验证请求头结果的变量初始化为真
        """
        header = self.request.headers
        appoint_header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                         'Accept-Encoding': 'gzip, deflate',
                         'Host': 'httpbin.org',
                         'Referer': 'http://httpbin.org',
                         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
                         }
        lock = True
        header = dict(header)
        for key in appoint_header:
            if appoint_header[key] !=header[key]:
                lock = False
                break
        if lock:
            data = {
                      "headers": header,
                    }
            self.write(data)
        else:self.write("Your request header is not correct!")