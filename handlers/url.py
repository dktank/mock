import handlers.handlers as hdl

urls = [
       (r'/', hdl.IndexHandler),
       (r'/get', hdl.Get149Handler),
       (r'/post', hdl.POST145Handler),
       (r'/headers', hdl.Headers137Handler),
       (r'/status/201',hdl.Status201Handler),
       (r'/status/400',hdl.Status400Handler),
       (r'/status/500',hdl.Status500Handler),
       (r'/cookies/set',hdl.Cookies_setHandler)
      ]