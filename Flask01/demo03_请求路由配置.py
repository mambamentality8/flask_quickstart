#1.导入Flask类
from flask import Flask

#2.创建Flask对象接收一个参数__name__，它会指向程序所在的包
from flask import request

app = Flask(__name__)

# 配置对象，里面定义需要给 APP 添加的一系列配置
class Config(object):
    DEBUG = True

# 从配置对象中加载配置
app.config.from_object(Config)

#3.装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    return 'Hello World'

#一.指定路由地址
#===========================================================
@app.route('/demo1')
def demo1():
    return 'demo1'

#二.给路由传参示例
#===========================================================
# 路由传递参数,字符串,不指定path默认就是字符串
@app.route('/user/<path:user_id>')
def user_info2(user_id):
    return 'hello %s 2222' % user_id

# 路由传递参数,整数
@app.route('/user/<int:user_id>')
def user_info1(user_id):
    return 'the num is %d 1111' % user_id

#三.指定请求方式
#===========================================================
@app.route('/demo2', methods=['GET', 'POST'])
def demo2():
    # 直接从请求中取到请求方式并返回
    return request.method

#4.Flask应用程序实例的run方法,启动WEB服务器
if __name__ == '__main__':
    app.run()