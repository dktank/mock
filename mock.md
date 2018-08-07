|URL|请求类型|返回内容|返回内容格式|备注|
|:---:|:---:|:---:|:---:|:---:|
|/get|get|1|JSON字符串|No.136|
|/get?k1=v1&k2=v2|get|2|JSON字符串|No.137<br>带参数type=1&page=1|
|/post|post|3|JSON字符串|No.137<br>带参数k1=v1&k2=v2|
|/headers|get|4|JSON字符串|No.138<br>指定请求头内容，然后发起请求|
|/post|post|5|JSON字符串|No.141<br>带参数<br>{'k2': 'v2', 'k1': ['v1', 'v3']}|
|/get?type=1&page=1|get|6|JSON字符串|No.142<br>带参数type=1&page=1|
|/get?type=1&page=2|get|7|JSON字符串|No.142<br>带参数type=1&page=2|
|/get?type=2&page=1|get|8|JSON字符串|No.142<br>带参数type=2&page=1|
|/get?type=2&page=2|get|9|JSON字符串|No.142<br>带参数type=2&page=2|
|/post|post|10|JSON字符串|No.145<br>指定请求头内容，然后发起请求|
|/get|get|11|JSON字符串|No.149<br>带参数{'name':'张三', 'hobbies': ['篮球','足球','羽毛球'], 'transcripts':{'语文':30, '数学': 99.5}}|
|/status/201|get|12|INT str|No.139<br>发起请求后的响应为response|
|/status/400|get|13|INT str|No.139<br>发起请求后的响应为response|
|/status/500|get|14|INT str|No.139<br>发起请求后的响应为response|
|/cookies/set?passport=boyabigdata|-|15|-|No.145 <br>设置cookie，带参数passport=boyabigdata|










+ 1


{
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

+ 2



{
  "args": {
    "k1": "v1", 
    "k2": "v2"
  }, 
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Accept-Language": "zh-cn", 
    "Connection": "close", 
    "Cookie": "_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique=1; _gauges_unique_year=1", 
    "Host": "httpbin.org", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38"
  }, 
  "origin": "124.65.37.238", 
  "url": "http://httpbin.org/get?k1=v1&k2=v2"
}

+ 3

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "k1": "v1", 
    "k2": "v2"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Content-Length": "11", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/2.7"
  }, 
  "json": null, 
  "origin": "124.65.37.238", 
  "url": "http://httpbin.org/post"
}


+ 4


指定请求头

{'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
 'Accept-encoding': 'gzip, deflate',
 'Host': 'httpbin.org',
 'Referer': 'http://httpbin.org',
 'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
 
-----------------------------

{
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "Referer": "http://httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
  }
}

+ 5

{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "k1": [
      "v1", 
      "v3"
    ], 
    "k2": "v2"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Connection": "close", 
    "Content-Length": "17", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/2.7"
  }, 
  "json": null, 
  "origin": "124.65.37.238", 
  "url": "http://httpbin.org/post"
}

+ 6

{'args': {'page': '1', 'type': '1'},
 'headers': {'Accept-Encoding': 'identity',
  'Connection': 'close',
  'Host': 'httpbin.org',
  'User-Agent': 'Python-urllib/2.7'},
 'origin': '124.65.37.238',
 'url': 'http://httpbin.org/get?type=1&page=1'}
 
 + 7
 
 
{'args': {'page': '1', 'type': '2'},
 'headers': {'Accept-Encoding': 'identity',
  'Connection': 'close',
  'Host': 'httpbin.org',
  'User-Agent': 'Python-urllib/2.7'},
 'origin': '124.65.37.238',
 'url': 'http://httpbin.org/get?type=1&page=1'}
 
 + 8
 
 
{'args': {'page': '2', 'type': '1'},
 'headers': {'Accept-Encoding': 'identity',
  'Connection': 'close',
  'Host': 'httpbin.org',
  'User-Agent': 'Python-urllib/2.7'},
 'origin': '124.65.37.238',
 'url': 'http://httpbin.org/get?type=1&page=1'}
 
 + 9 
 
 
{'args': {'page': '2', 'type': '2'},
 'headers': {'Accept-Encoding': 'identity',
  'Connection': 'close',
  'Host': 'httpbin.org',
  'User-Agent': 'Python-urllib/2.7'},
 'origin': '124.65.37.238',
 'url': 'http://httpbin.org/get?type=1&page=1'}
 
 + 10

指定headers

{'Accept': '*/*',
 'Accept-Encoding': 'gzip, deflate',
 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
 'Cache-Control': 'no-cache',
 'Connection': 'keep-alive',
 'DNT': '1',
 'Host': 'httpbin.org',
 'Origin': 'http://httpbin.org',
 'Pragma': 'no-cache',
 'Referer': 'http://httpbin.org/forms/post',
 'Upgrade-Insecure-Requests': '1',
 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'}

-------------

{u'args': {},
 u'data': u'',
 u'files': {},
 u'form': {u'comments': u'\u5317\u4eac\u5e02\u6d77\u6dc0\u533a\u5317\u56db\u73af\u897f\u8def67\u53f7\u4e2d\u5173\u6751\u56fd\u9645\u521b\u65b0\u5927\u53a6603',
  u'custemail': u'service@boyabigdata.cn',
  u'custname': u'\u535a\u96c5\u5927\u6570\u636e\u5b66\u9662',
  u'custtel': u'010-62756975',
  u'delivery': u'18:00',
  u'size': u'large',
  u'topping': [u'mushroom', u'cheese']},
 u'headers': {u'Accept': u'*/*',
  u'Accept-Encoding': u'gzip, deflate',
  u'Accept-Language': u'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
  u'Cache-Control': u'no-cache',
  u'Connection': u'close',
  u'Content-Length': u'392',
  u'Content-Type': u'application/x-www-form-urlencoded',
  u'Cookie': u'passport=boyabigdata',
  u'Dnt': u'1',
  u'Host': u'httpbin.org',
  u'Origin': u'http://httpbin.org',
  u'Pragma': u'no-cache',
  u'Referer': u'http://httpbin.org/forms/post',
  u'Upgrade-Insecure-Requests': u'1',
  u'User-Agent': u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:43.0) Gecko/20100101 Firefox/43.0'},
 u'json': None,
 u'origin': u'124.65.37.238',
 u'url': u'http://httpbin.org/post'}
 
 + 11

{u'args': {u'profile': u'{"transcripts": {"\\u6570\\u5b66": 99.5, "\\u8bed\\u6587": 30}, "name": "\\u5f20\\u4e09", "hobbies": ["\\u7bee\\u7403", "\\u8db3\\u7403", "\\u7fbd\\u6bdb\\u7403"]}'},
 u'headers': {u'Accept': u'*/*',
  u'Accept-Encoding': u'gzip, deflate',
  u'Connection': u'close',
  u'Host': u'httpbin.org',
  u'User-Agent': u'python-requests/2.18.4'},
 u'origin': u'124.65.37.238',
 u'url': u'http://httpbin.org/get?profile={"transcripts"%3A+{"\\u6570\\u5b66"%3A+99.5%2C+"\\u8bed\\u6587"%3A+30}%2C+"name"%3A+"\\u5f20\\u4e09"%2C+"hobbies"%3A+["\\u7bee\\u7403"%2C+"\\u8db3\\u7403"%2C+"\\u7fbd\\u6bdb\\u7403"]}'}
 
 + 12
 
 response.code 201 <br>response.msg 'CREATED'
 
 + 13
 
 response.code 400 <br>response.msg 'BAD REQUEST'
 
 + 14
 
 response.code 500 <br>response.msg 'INTERNAL SERVER ERROR'