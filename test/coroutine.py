from gevent import monkey; monkey.patch_socket()
import gevent
import requests


lis = []
def f(req_url):
    try:
        reqr = requests.get(req_url)
        text = reqr.json()
        print(text)
    except Exception as e:
        lis.append(1)
        len1 =  len(lis)
        print("*"*len1+str(len1),e)
        print(str(len1),e)
spa_list = []
for i in range(1500):
    url =  'http://httpbin.org/get?i='+str(i)
    spa_list.append(gevent.spawn(f,url))
gevent.joinall(spa_list)
