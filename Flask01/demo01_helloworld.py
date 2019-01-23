#1.导入Flask类
from flask import Flask

#2.创建Flask对象接收一个参数__name__，它会指向程序所在的包
app = Flask(__name__)

#3.装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    return 'Hello World'

#4.Flask应用程序实例的run方法,启动WEB服务器
if __name__ == '__main__':
    app.run()