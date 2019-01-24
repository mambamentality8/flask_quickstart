"""
访问地址的时候加上动态参数

- 格式: @app.route("地址/<参数类型:变量>")
- 常见的参数类型
  - int	 整数
  - float 小数
  - path 字符串(默认就是)

"""""

from flask import Flask

app = Flask(__name__)

#1,接收一个整数
@app.route('/int_number/<int:age>')
def int_number(age):

    return "the int age is %s"%age

#2,接收一个小数
@app.route('/float_number/<float:age>')
def float_number(age):

    return "the float age is %s"%age

#3,接收一个字符串
@app.route('/int_number/<name>')
def path_number(name):

    return "the path name is %s"%name

if __name__ == '__main__':
    app.run()