from flask import Flask,render_template,flash

app = Flask(__name__)

"""
宏：
概念：模板中的函数；
作用：封装复用模板页面中的功能代码，一般用来实现动态的功能代码(继承复用的使用模板页面固定不变的代码块)。
使用：关键字macro;只能在模板中使用。
if、for/raise/try:except/assert/def/class/
需求：实现登录表单；文本框、密码框、表单按钮

区别：
1、宏用来实现动态功能代码的封装
2、继承用来实现静态功能代码的封装

url_for:接收的参数是函数名(端点endpoint)

"""
@app.route('/')
def index():
    return render_template('demo2_macro.html')


if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)