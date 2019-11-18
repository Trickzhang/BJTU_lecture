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


class Spider(object):
    def __init__(self, url, start_time, name, student_id):
        self._get_url = url
        self._start_time = start_time
        self._name = name
        self._student_id = student_id
        self._reset_count = 2
        self._delay_time = 1
        self._xmt_time = 0.4
        self._send_flag = False
        self._session = requests.Session()
        self._post_url = 'http://ynz14wo02p6hjfv9.mikecrm.com/handler/web/form_runtime/handleSubmit.php'
        self._user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        self._get_headers = {
            'User-Agent':self._user_agent,
        }
        self._csv = {
                    'r':'',
                    'c':{
                        'cp':{}
                        },
                    }
        self._response = ""
                
    def run(self):
        print(self._start_time)
        while self._send_flag == False:
            self.check_time()
        
        time.sleep(self._delay_time)
        while self._send_flag and self._reset_count:
            self.post_data()
            self._reset_count -= 1
        
        return self.check_result()
   
    def check_time(self):
        dt = datetime.datetime.now()
        schel_time = dt.strftime('%Y-%m-%d %H:%M:%S')
        if (schel_time == self._start_time):
            time.sleep(self._delay_time)
            self._send_flag = True
        
    def post_data(self):
        response = self._session.get(self._get_url, headers=self._get_headers)
        result = response.content.decode('utf-8')
        
        try:
            cookies = response.cookies
            cookie = cookies.items()[0][1]
            re_result = re.search(r'"cpo":"(\d+);(\d+);(\d+)".*?"FRS":(\d+),"ACC":"(.*?)","T":"(.*?)","I":(\d+)', result)
            
            self._csv['c']['cp'][re_result.group(2)] = self._name
            self._csv['c']['cp'][re_result.group(3)] = self._student_id
            self._csv['s'] = int(re_result.group(4))
            self._csv['acc'] = re_result.group(5)
            self._csv['t'] = re_result.group(6)
            self._csv['i'] = int(re_result.group(7))

            self._csv['fc'] = self.encrypt(cookie, self._csv['t'])

            data = {"cvs":self._csv}
            post_data = str(json.dumps(data))

        except Exception as e:
            print(e)
            time.sleep(self._xmt_time)
            return
        
        self._response = self._session.post(self._post_url, headers=self._get_headers, data={'d': post_data})
        self._send_flag = False
        
    def check_result(self):
        if self._response:
            content = json.loads(self._response.content)
            if content['r'] == 0:
                return True
            else:
                return False
            
        else:
            return False

    def encrypt(self, form_data, we):
        with open('./fc.js') as f:
            js = execjs.compile(f.read())
            return js.call('X', form_data, we)
