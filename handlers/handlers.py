import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello,get")
        #self.render('input.html')

class ContentHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("hello,post")
        # inpcont = self.get_argument('inpcont')
        # inpcont1 = self.get_argument('inpcont1')
        # self.render('content.html', content={"name":inpcont,"password":inpcont1})
