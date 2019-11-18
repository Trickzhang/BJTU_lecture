# -*- coding:utf-8 -*-
'''
Author: Trick
Email: Trick_life@163.com
'''

import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from form import Ui_Form
from lecture import Spider
import threading
import time


class mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.student_info = []
        self.thread = []
        self.main_thread = ""
        self.result = []
        
    def add(self):
        url = self.ui.url_text.text()
        time = self.ui.time_text.text()
        name = self.ui.name_text.text()
        student_id = self.ui.id_text.text()
        
        self.student_info.append([name, student_id])
        
        t = threading.Thread(target=self.post, args=(url, time, name, student_id))
        t.daemon = True
        t.start()
        self.thread.append(t)
        
        self.print_info()
        
        
    def confirm(self):
        self.check_alive(self.thread)
        
    def print_info(self):
        self.result_text = '请求队列信息如下：\n'
        for name, student_id in self.student_info:
            self.result_text += name +" " + student_id + " 加入队列\n"
        self.ui.result_text.setText(self.result_text)
        
    def check_alive(self, thread_list):
        # while True:
        #    for t in thread_list:
        #         if(t.is_alive()):
        #             time.sleep(1)
        #             break
        #     else:
        #         break
        for t in thread_list:
            if(t.is_alive()):
                return
        self.result_text = "结果显示:\n"
        for name, student_id, flag in self.result:
            if flag:
                flag = "成功"
            else:
                flag = "失败"
            self.result_text += name +" " + student_id + " " + flag+"\n"
        self.ui.result_text.setText(self.result_text)
    
    def post(self, url, time, name, student_id):
        spider = Spider(url, time, name, student_id)
        self.result.append([name, student_id, spider.run()])
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    md = mywindow()
    md.show()
    sys.exit(app.exec_())
    
# self.ConfirmButton.clicked.connect(Form.confirm)
# self.CancleButton.clicked.connect(Form.cancle)