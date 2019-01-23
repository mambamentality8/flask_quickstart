#1.导入Flask类
from flask import Flask, jsonify

#2.创建Flask对象接收一个参数__name__，它会指向程序所在的包
from flask import redirect
from flask import request
from flask import url_for

app = Flask(__name__)

# 配置对象，里面定义需要给 APP 添加的一系列配置
class Config(object):
    DEBUG = True

# 从配置对象中加载配置
app.config.from_object(Config)

# 生成json数据响应体
@app.route('/demo4')
def demo4():
    json_dict = {
        "user_id": 10,
        "user_name": "laowang"
    }
    return jsonify(json_dict)

# 重定向
@app.route('/demo5_1')
def demo5_1():
    return redirect('https://www.baidu.com')

# 反解析
@app.route('/demo1')
def demo1():
    return 'demo1'

@app.route('/demo5_2')
def demo5_2():
    return redirect(url_for('demo1'))

#====================================
# 路由传递参数
@app.route('/user/<int:user_id>')
def user_info(user_id):
    return 'hello %d' % user_id

# 重定向
@app.route('/demo5_3')
def demo5_3():
    # 使用 url_for 生成指定视图函数所对应的 url
    return redirect(url_for('user_info', user_id=100))

@app.route('/demo6')
def demo6():
    return '状态码为666',888


#4.Flask应用程序实例的run方法,启动WEB服务器
if __name__ == '__main__':
    app.run()