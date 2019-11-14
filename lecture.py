# -*- coding:utf-8 -*-
'''
Author: Trick
Email: Trick_life@163.com
'''
import requests
import json
import execjs
import re
import datetime
import time


get_url = "讲座URL"
start_time = "讲座开抢时间"  # 格式2019-11-14 09:00:00
delay_time = 0.2  # int/float类型，延迟以后发送get请求

username = "姓名"
student_id = "学号"

reset_count = 3

print(username)
print(student_id)
print(start_time)


def encrypt(form_data, we):
	with open('./fc.js') as f:
		js = execjs.compile(f.read())
		return js.call('X', form_data, we)


cvs = {
	'r':'',
	'c':{
		'cp':{}
	},
}


post_url = 'http://ynz14wo02p6hjfv9.mikecrm.com/handler/web/form_runtime/handleSubmit.php'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
get_headers = {
	'User-Agent':user_agent,
}

session = requests.Session()


while reset_count:
	dt = datetime.datetime.now()
	schel_time = dt.strftime('%Y-%m-%d %H:%M:%S')
	if schel_time == start_time or reset_count < 3:
		if(reset_count == 3):
			time.sleep(delay_time)

		response = session.get(get_url, headers=get_headers)
		result = response.content.decode('utf-8')
		
		try:
			cookies = response.cookies
			cookie = cookies.items()[0][1]
			re_result = re.search(r'"cpo":"(\d+);(\d+);(\d+)".*?"FRS":(\d+),"ACC":"(.*?)","T":"(.*?)","I":(\d+)', result)
			

			cvs['c']['cp'][re_result.group(2)] = username
			cvs['c']['cp'][re_result.group(3)] = student_id
			cvs['s'] = int(re_result.group(4))
			cvs['acc'] = re_result.group(5)
			cvs['t'] = re_result.group(6)
			cvs['i'] = int(re_result.group(7))

			cvs["fc"] = encrypt(cookie, cvs['t'])

			data = {"cvs":cvs}
			post_data = str(json.dumps(data))
		
		except Exception as e:
			print(e)
			reset_count -= 1
			time.sleep(0.4)
			continue

		response = session.post(post_url, headers=get_headers, data={'d': post_data})
		print(reset_count)
		print(datetime.datetime.now())
		print(username, student_id, response.content)

		break
print(reset_count)




