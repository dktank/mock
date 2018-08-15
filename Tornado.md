#Tornado 

## 1、介绍
> Tornado 是一个Python web框架和异步网络库 起初由 FriendFeed 开发. 通过使用非阻塞网络I/O, Tornado 可以支持上万级的连接，处理 长连接, WebSockets, 和其他 需要与每个用户保持长久连接的应用。
#### Tornado 大体上可以被分为4个主要的部分:
 - web框架 (包括创建web应用的RequestHandler类，还有很多其他支持的类)     
 - HTTP的客户端和服务端实现 (HTTPServer and AsyncHTTPClient).
 - 异步网络库 (IOLoop and IOStream), 为HTTP组件提供构建模块，也可以用来实现其他协议.
 - 协程库 (tornado.gen) 允许异步代码写的更直接而不用链式回调的方式.
 
## 2、web框架
> 1、tornado.web 提供了一种带有异步功能并允许它扩展到大量开放连接的 简单的web 框架,可以处理长连接(long polling) 
```
##简单示例
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```
> 2、**RequestHandler**：HTTP请求处理的基类。
 3、RequestHandler.get_argument(name, default=[], strip=True)：
>>返回指定的name参数的值.
  如果没有提供默认值, 那么这个参数将被视为是必须的, 并且当 找不到这个参数的时候我们会抛出一个 MissingArgumentError.
  如果一个参数在url上出现多次, 我们返回最后一个值.
  返回值永远是unicode.

> 4、RequestHandler.get_arguments(name, strip=True):
>> 返回指定name的参数列表.
   如果参数不存在, 返回一个空列表.
   返回值永远是unicode.

> 5、RequestHandler.get_query_argument(name, default=[], strip=True)：
>> 从请求的query string返回给定name的参数的值.
如果没有提供默认值, 这个参数将被视为必须的, 并且当找不到这个 参数的时候我们会抛出一个 MissingArgumentError 异常.
如果这个参数在url中多次出现, 我们将返回最后一次的值.
返回值永远是unicode.

> 6、RequestHandler.get_query_arguments(name, strip=True):
>> 返回指定name的参数列表.
如果参数不存在, 将返回空列表.
返回值永远是unicode.

>7、RequestHandler.get_body_argument(name, default=[], strip=True)
>> 返回请求体中指定name的参数的值.
   如果没有提供默认值, 那么这个参数将被视为是必须的, 并且当    找不到这个参数的时候我们会抛出一个 MissingArgumentError.
   如果一个参数在url上出现多次, 我们返回最后一个值.
   返回值永远是unicode.

>8、RequestHandler.get_body_arguments(name, strip=True)
>>返回由指定请求体中指定name的参数的列表.
  如果参数不存在, 返回一个空列表.
  返回值永远是unicode.

>10、RequestHandler.request属性和方法:(除非另有说明,所有属性都是str）
>>method:请求方法，例如：“GET” or “POST”
  uri：请求的uri，例如："/get?type=1&page=1"
  path：uri中的path，例如：/get
  query：uri中的query，例如：type=1&page=1
  version：请求中指定的HTTP版本，例如：HTTP/1.1
  headers：请求的headers
  body：请求的body，返回类型是字节串
  remote_ip：客户端IP
  protocol：协议类型，例如： “http” or “https”
  host：请求的主机名，例如：127.0.0.1:8008
  arguments：获得GET/POST参数，例如：{'type':[b'1'],'page': [b'1']}
  cookies：cookies，以字典形式出现== RequestHandler.cookies
  full_url()：重构url，例如:http://127.0.0.1:8008/get?type=1&page=1
  request_time()：返回执行此请求所需的时间
  get_ssl_certificate：返回客户端的SSL证书（如果有的话）
  query_arguments，body_arguments，files，connection

>11、tornado.httputil.url_concat(url, args)：组合URL和参数
 12、tornado.httputil.format_timestamp(ts)：以HTTP使用的格式格式化时间戳。 例子：
 >> format_timestamp(1359312200)
'Sun, 27 Jan 2013 18:43:20 GMT'

>13、RequestHandler.set_status(status_code, reason=None)：
设置响应的状态码：reason (string) –用人类可读的原因短语来描述状态码
>14、RequestHandler.set_header(name, value):给响应设置指定的头部和对应的值.
>15、RequestHandler.add_header(name, value)：添加指定的响应头和对应的值.
>16、RequestHandler.clear_header(name):清除输出头, 取消之前的 set_header 调用,不适用于被 add_header 设置了多个值的头.
>17、RequestHandler.write(chunk):把给定块写到输出buffer
>18、RequestHandler.flush(include_footers=False, callback=None):将当前输出缓冲区写到网络.
>19、RequestHandler.finish(chunk=None)：完成响应, 结束HTTP 请求.
>20、RequestHandler.render(template_name, **kwargs):使用给定参数渲染模板并作为响应.
>21、RequestHandler.render_string(template_name, **kwargs):使用给定的参数生成指定模板.返回生成的字节字符串(以utf8). 为了生成并写一个模板 作为响应, 使用上面的render()
>22、RequestHandler.get_template_namespace()：返回一个字典被用做默认的模板命名空间.
>23、RequestHandler.redirect(url, permanent=False, status=None):重定向到给定的URL(可以选择相对路径).
>24、RequestHandler.send_error(status_code=500, **kwargs)给浏览器发送指定的HTTP错误码
>25、RequestHandler.clear():重置这个响应的所有头部和内容.
>26、RequestHandler.get_cookie(name, default=None):获取给定name的cookie值, 如果未获取到则返回默认值.
>27、RequestHandler.set_cookie(name, value, domain=None, expires=None, path='/', expires_days=None, **kwargs)：设置给定的cookie 名称/值，和其他
>28、RequestHandler.clear_cookie(name, path='/', domain=None)：删除给定名称的cookie
>29、RequestHandler.clear_all_cookies(path='/', domain=None)：删除用户在本次请求中所有携带的cookie.
>30、RequestHandler.set_secure_cookie(name, value, expires_days=30, version=None, **kwargs)：给cookie签名和时间戳以防被伪造.
>31、RequestHandler.get_secure_cookie(name, value=None, max_age_days=31, min_version=None):如果给定的签名过的cookie是有效的,则返回，否则返回None.

 >32、tornado.httputil.parse_request_start_line(line)：例子：
 >>  parse_request_start_line("GET /foo HTTP/1.1")
RequestStartLine(method='GET', path='/foo', version='HTTP/1.1')

>33、tornado.httputil.parse_response_start_line(line):例子：
>> parse_response_start_line("HTTP/1.1 200 OK")
ResponseStartLine(version='HTTP/1.1', code=200, reason='OK')

----------
## tornado.httpserver — 非阻塞 HTTP server
>1、tornado.httpserver.HTTPServer(*args, **kwargs)：非阻塞，单线程 HTTP server。
>2、简单的单进程:
>> server = HTTPServer(app)
   server.listen(8888)
   IOLoop.current().start()
 
>3、 简单的多进程
>>server = HTTPServer(app)
server.bind(8888)
server.start(0)  # Fork 多个子进程
IOLoop.current().start()

>4、高级多进程
>>sockets = tornado.netutil.bind_sockets(8888)
tornado.process.fork_processes(0)
server = HTTPServer(app)
server.add_sockets(sockets)
IOLoop.current().start()
##tornado.httpclient — 异步 HTTP 客户端
>1、tornado.httpclient.HTTPClient(async_client_class=None, **kwargs)一个阻塞的 HTTP 客户端.
>>close():关闭该 HTTPClient, 释放所有使用的资源.
>>fetch(request, **kwargs):执行一个请求, 返回一个 HTTPResponse 对象.

>2、class tornado.httpclient.AsyncHTTPClient:一个非阻塞 HTTP 客户端.
>>close():销毁该 HTTP 客户端, 释放所有被使用的文件描述符.
>>fetch(request, callback=None, raise_error=True, **kwargs)
执行一个请求, 并且异步的返回 HTTPResponse.
```
##使用示例
def handle_request(response):
    if response.error:
        print "Error:", response.error
    else:
        print response.body

http_client = AsyncHTTPClient()
http_client.fetch("http://www.google.com/", handle_request)
```


  
  

  




 





