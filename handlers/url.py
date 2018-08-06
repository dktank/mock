from handlers import IndexHandler,Handler136,Handler137,Handler138,Handler139,Handler141,Handler142,Handler145,Handler149

urls = [
       (r'/',IndexHandler.IndexHandler),
       (r'/get', Handler137.GetHandler),
       (r'/post', Handler137.PostHandler),
       (r'/headers', Handler138.GetHandler),
       (r'/status/201',Handler139.Status201Handler),
       (r'/status/400',Handler139.Status400Handler),
       (r'/status/500',Handler139.Status500Handler),
       (r'/cookies/set',Handler145.SetCookiesHandler)
      ]