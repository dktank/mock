import tornado.web
from handlers import url
from config import setting

application = tornado.web.Application(
    handlers= url.urls,
    **setting.file_setting
)