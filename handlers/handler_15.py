from config.public import Request


class SetCookiesHandler(Request):
    """该Handler完成编号10协议：|/cookies/set?passport=boyabigdata|-|-|-|No.145 <br>设置cookie，带参数passport=boyabigdata|"""

    def get(self):
        """处理GET请求

        变量passport存放请求中的passport参数，设置cookie的值为passport
        """
        try:
            passport = self.get_argument("passport")
            self.set_secure_cookie("passport", passport)
        except:
            self.write("No target parameters were found")
