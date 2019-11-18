# BJTU_lecture
## 声明：本脚本仅用作学习交流，不可用于任何商业用途
利用python爬虫中模拟登陆的原理，解析麦克表单，制作自动抢讲座脚本  

## 使用方法  
1. **环境搭建**  
  * pip install -i https://pypi.douban.com/simple requests  
  * pip install -i https://pypi.douban.com/simple PyExecJS  
  * pip install -i https://pypi.douban.com/simple PyQt5  
2. **脚本运行**  
在CMD命令窗口下输入python main.py，在弹出的form窗口中顺序输入以下值，并点击添加即可
  * URL： 本次讲座的URL  
  * 时间： 本次讲座的开抢时间，格式 2019-11-11 11:11:11  
  * 姓名： 你的名字  
  * 学号： 你的学号  
3. **说明**  
右侧信息框显示操作结果。内部采用多线程方法，单次可以同时为多位同学代抢，点击查询按钮查看结果  
trick利用pyinstaller生成了对应的exe，但文件有35M，而github单个文件最大支持25M，因此不想安装python环，又想使用该脚本的朋友可以发送email到trick_life@163.com。trick看到后会发送给你exe文件


