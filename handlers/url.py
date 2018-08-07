from handlers import handler_index,handler_1,handler_3,handler_4,handler_12,handler_5,handler_6,handler_10,handler_11,handler_15,handler_13,handler_14

urls = [
       (r'/',handler_index.IndexHandler),
       (r'/get', handler_11.GetHandler),
       (r'/post', handler_10.PostHandler),
       (r'/headers', handler_4.GetHandler),
       (r'/status/201',handler_12.Status201Handler),
       (r'/status/400',handler_13.Status400Handler),
       (r'/status/500',handler_14.Status500Handler),
       (r'/cookies/set',handler_15.SetCookiesHandler)
      ]