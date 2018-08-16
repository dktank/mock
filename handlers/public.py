from config.rewrite import RequestHandler
import requests
class Request(RequestHandler):
    """获取的用户请求基本信息，集合成字典并返回"""

    def get_result1(self,data):
         """在GET请求处理并返回信息"""

         url = self.request.full_url()
         query = self.request.query
         args = Parse_args.parse_query(self,query)

         ##根据请求修改data里的数据
         data["args"] = args
         data["url"] = url
         data["origin"] = "192.168.1.1"
         if len(args)!=0:
             data["headers"] = {
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "zh-cn",
                                "Connection": "close",
                                "Cookie": "_gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique=1; _gauges_unique_year=1",
                                "Host": "httpbin.org",
                                "Upgrade-Insecure-Requests": "1",
                                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38"
                              }
         data["headers"]["Host"] = "hackdata.cn"
         return data



    def post_result1(self,data):
         """在POST请求处理并返回信息"""

         url = self.request.full_url()
         body = self.request.body.decode("utf-8")
         form = Parse_args.parse_body(self,body)
         ##根据请求修改data里的数据

         data["form"] = form
         data["headers"]["Host"] = "hackdata.cn"
         data["origin"] = "192.168.1.1"
         data["url"] = url
         return data



class Parse_args():
    '''该类功能是解析请求参数，返回对应的字典形式'''

    def parse_query(self,query_str):
        args = {}
        try:
            query_strs = query_str.split("&")
            args_list = []
            for item in query_strs:
                try:
                    item_list = item.split("=")
                    args_list.append(item_list)
                except:
                    pass
            args = dict(args_list)
            return args
        except:
            return args


    def parse_body(self,body_str):
        form = {}
        try:
            query_strs = body_str.split("&")
            args_list = []
            for item in query_strs:
                try:
                    item_list = item.split("=")
                    args_list.append(item_list)
                except:
                    pass
            length = len(args_list)
            form = dict(args_list)
            for item in form.keys():
                for i in range(length):
                    if args_list[i][0] == item and (args_list[i][1] != form[item]):
                        if not isinstance(form[item],list):
                            li = [args_list[i][1],form[item]]
                            form[item] = li
                        elif (args_list[i][1] not in form[item]):
                            form[item].insert(-2,args_list[i][1])
            return form
        except:
            return form








