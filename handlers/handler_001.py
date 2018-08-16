from handlers.public import Request

class GetHandler(Request):
    '''该Handler完成编号1、2两个协议：
            |/httpbin/get|get|1|JSON|No.136|和|/httpbin/get?k1=v1&k2=v2|get|2|JSON|No.137<br>带参数type=1&page=1|
    '''
    def get(self):
        """处理GET请求,允许url带参数"""
        data = {
                  "args": {},
                  "headers": {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
                    "Connection": "close",
                    "Cookie": "_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
                    "Host": "httpbin.org",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
                  },
                  "origin": "124.65.37.238",
                  "url": "http://httpbin.org/get"
                }
        res_data = Request.get_result1(self,data)
        self.write(res_data)

