import handlers.handlers as hdl

urls = [
       (r'/', hdl.IndexHandler),
       (r'/get', hdl.Get2Handler),
       (r'/post', hdl.POST2Handler),
       (r'/headers', hdl.HeadersHandler),
       (r'/status/201',hdl.Status201Handler),
       (r'/status/400',hdl.Status400Handler),
       (r'/status/500',hdl.Status500Handler)
      ]