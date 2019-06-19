#coding=utf-8

import sys  
reload(sys)  
sys.setdefaultencoding('ISO-8859-1')  



from bottle import get,post,run,request,template
 
 
@get("/")
def index():
	return template("index") 
#### 这个是 客户端请求 服务端就发给一个 index.html 控制界面给客户端
@post("/cmd")
def cmd():
	adss=request.body.read().decode()#### 接收到 客户端 发过来的数据
	print("press:"+adss)
	main(adss)  #### 传值到主函数 实现对应功能
	return "OK"
run(host="0.0.0.0")  #### 开启服务端 
