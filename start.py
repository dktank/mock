import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from App import application
from tornado.options import define, options

define("port", default=8008, help="run on the given port", type=int)

def run():
    #tornado.options.define("log_file_prefix", default="./log/runlog.log")
    tornado.options.parse_command_line()
    app = application.application
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    run()
