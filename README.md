# BJTU_lecture
## 声明：本脚本仅用作学习交流，不可用于任何商业用途
利用python爬虫中模拟登陆的原理，解析麦克表单，制作自动抢讲座脚本  

### 用文本编辑器打开lecture.py，修改下述变量  
1. get_url:  填入本次讲座的url地址。  
2. start_time:  填入讲座开抢时间。  
3. delay_time:  填入检测到时延长时间。设定本变量的原因是判断到时机制为start_time与本地时钟相等。但实际应该判断start_time与服务器时间相等，而本地时钟与服务器时钟并不能保证相等。start_time+delay_time是本地发起请求的实际时间。   
4. username:  填入你的姓名。  
5. student_id:  填入你的学号。
6. reset_count:  表示发送请求次数(不建议修改此值，该值较大时容易被封IP)。  

将fc.js与lecture.py放在同一路径下，打开CMD，并cd到此目录，输入python lecture.py等待结果输出。  
### 成功判定方法  
如果输出 姓名 学号 b'{"r":0}'则表示抢成功。  
如果输出中括号内值不为0，说明速度太慢，本次名额已满，考虑降低delay_time值。  
如果'NoneType' object has no attribute 'group'信息打印三次，说明delay_time太小，发送三次请求，表单都尚未开放填写，考虑适当增大delay_time值。  

fc.js是由javascrapt语言编写的加密算法文件。在发送请求时，fc字段的值就是通过该算法生成的。  
### 目前该脚本存在不足如下：
1. delay_time值难以设定。trick通常在表单开放前十分钟，多次请求，将本地接收时间与response携带的head时间相减，取平均作为delay_time值。trick经验值取0.5，与trick竞争者通常为手速，因此屡试不爽。  
2. 表单格式固定，当修改表单结构，例如需要填写手机号信息时，该脚本失效。

