#coding:utf-8
import requests,json,re,hashlib,uuid

def get_message():
	url = 'http://www.dc2n.com/json/sms/Submit'
	data ={"account":"602221",
	"password":"a414e00d0370a6d5ce12e6f1e019b5bb",
	"msgid":"74b53e23d6ae989d4c5636b2b730",
	"phones":"18321028517",
	"content":"测试给你发来链接https://s.ikandy.cn/eED7k ，点击链接进入智慧同屏，随时随地快速直观的解决您的问题！链接24小时有效",
	"sign":"【甜新科技】","subcode":"",
	"sendtime":"201405051230"
	}
	r = requests.post(url,json=data)
	print(r.text)
if __name__ == '__main__':
	a = hashlib.md5(b"wbjYh24F").hexdigest()
	print(uuid.uuid5(uuid.NAMESPACE_URL,"测试给你发来链接https://s.ikandy.cn/eED7k ，点击链接进入智慧同屏，随时随地快速直观的解决您的问题！链接24小时有效"))
	get_message()

		