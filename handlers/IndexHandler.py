from config.RewriteRequestHandler import RequestHandler

#索引处理器
class IndexHandler(RequestHandler):
    def get(self):
        self.render("input.html")
