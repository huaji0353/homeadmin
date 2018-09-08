# coding:utf-8
'''
tp-link homeadmin.py
orgin code: https://github.com/XX-net/XX-Net/issues/10283#issuecomment-377671198
modify by: github@huaji0353

# 重写格式化format
'''
cfg = {
	"ip":"192.168.1.1", 
	"pwd":"114514"
}
try:
	cfg = __import__("config").cfg
except:
	print("no config!!!")
	exit(0)
route_ip = cfg["ip"]

import os
os.environ.pop('HTTP_PROXY', None)
os.environ.pop('HTTPS_PROXY', None)

import requests
import json
import time
from pdb import set_trace as debug

headers = {
	'Host':'tplogin.cn',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
	'Accept':'application/json, text/javascript, /; q=0.01',
	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate',
	'Content-Type':'application/json; charset=UTF-8',
	'X-Requested-With':'XMLHttpRequest',
	'Referer':'http://tplogin.cn/',
	'Content-Length':'54',
	'Connection':'keep-alive'
}
# 构造登录请求
Payload = {
	"method":"do",
	"login":{"password":cfg["pwd"]}
}

# 获取token
url = "http://{route_ip}/".format(route_ip=route_ip)
html = requests.post(url, json=Payload, headers=headers, verify = False)
print(html.headers)
# 组合token成标准url进行POST请求
stok = json.loads(html.text)["stok"]
full_url = "{url}stok={stok}/ds".format(url=url,stok=stok)
# 构造并请求POST json表单
Payload = {"hosts_info":{"table":"host_info"},"method":"get"}
headers['Content-Length'] = '42'
p = requests.post(url=full_url, json=Payload, headers=headers).json()
debug()
print(p)
# done
exit(0)