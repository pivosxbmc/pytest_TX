#coding:utf-8
import requests,json,re,hashlib,uuid

def get_message():
	url = 'http://www.dc2n.com/json/sms/Submit'
	data ={"account":"602xxxx",
	"password":"a414e00d0370a6d5ce12e6f1e019xxxx",
	"msgid":"3a85a318ea205b6c8cf31f4cd08fxxxx",
	"phones":"1832102xxxx",
	"content":"耿媛嘿嘿给你发来链接https://s.ikandy.cn/eED7kxx ，点击链接进入智慧同屏，随时随地快速直观的解决您的问题！链接24小时有效",
	"sign":"【甜新科技】","subcode":"",
	"sendtime":"201405051230"
	}
	r = requests.post(url,json=data)
	print(r.text)
if __name__ == '__main__':
	a = hashlib.md5(b"wbjYh24F").hexdigest()
	print(uuid.uuid5(uuid.NAMESPACE_URL,"耿媛嘿嘿给你发来链接https://s.ikandy.cn/eED7kxx ，点击链接进入智慧同屏，随时随地快速直观的解决您的问题！链接24小时有效"))
	get_message()

		