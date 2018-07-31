import handlers.handlers as hdl

urls = [(r'/get', hdl.IndexHandler),
       (r'/post', hdl.ContentHandler)
      ]