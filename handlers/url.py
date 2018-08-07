from handlers import IndexHandler,Handler_1,Handler_2,Handler_3,Handler_4,Handler_139,Handler_5,Handler_6,Handler_10,Handler_11

urls = [
       (r'/',IndexHandler.IndexHandler),
       (r'/get', Handler_11.GetHandler),
       (r'/post', Handler_10.PostHandler),
       (r'/headers', Handler_4.GetHandler),
       (r'/status/201',Handler_139.Status201Handler),
       (r'/status/400',Handler_139.Status400Handler),
       (r'/status/500',Handler_139.Status500Handler),
       (r'/cookies/set',Handler_10.SetCookiesHandler)
      ]