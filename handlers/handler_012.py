from handlers.public import Request

class  GetHandler(Request):
    """该Handler完成编号12,16,17,18,19协议
       |/douban/tag/%E8%8B%B1%E5%9B%BD%20%E5%96%9C%E5%89%A7%202015|get|12|html|No.143 验证参数{'start':'20','type':'S'}|
       16，17，18，19协议按照path返回不同页面
    """

    def get(self,tag_name):
        """处理GET请求"""

        verification_tag =  r"英国 喜剧 2015"
        #判断tag_name是否为"英国 喜剧 2015",如果是检查该链接参数
        if tag_name ==verification_tag:
            if Request.verification_query(self):
                tag_name = tag_name+".html"
                self.render(tag_name)
            else:
                self.set_status(status_code=404)
        else:
            tag_name = tag_name+".html"
            self.render(tag_name)



