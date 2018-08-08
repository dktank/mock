from handlers import handler_001,handler_003,handler_004,handler_012,handler_005,handler_006,handler_010,handler_011,handler_015,handler_013,handler_014

urls = [
        #处理get请求
       (r'/get', handler_011.GetHandler),

        #处理post请求
       (r'/post', handler_010.PostHandler),

        #指定headers的请求
       (r'/headers', handler_004.GetHandler),

        #发送201状态码
       (r'/status/201',handler_012.Status201Handler),

        #发送400状态码
       (r'/status/400',handler_013.Status400Handler),

        #发送500状态码
       (r'/status/500',handler_014.Status500Handler),

        #设置cookies
       (r'/cookies/set',handler_015.SetCookiesHandler)
      ]