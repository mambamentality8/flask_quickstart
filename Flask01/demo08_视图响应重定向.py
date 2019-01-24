"""
返回redirect响应对象

- 格式: response = redirect('地址')
- 参数:
  - location: 方法中的第一个参数,可以是服务器内部地址,也可以外链地址
  - code: 默认值302(重定向的标识)


"""""
from flask import Flask,redirect

app = Flask(__name__)

#班长地址
@app.route('/address')
def banzhang():

    #1,调用redirect方法,生成响应体
    response = redirect("/inner")
    #response = redirect("http://www.taobao.com")

    return response

#班主任地址
@app.route('/inner')
def inner():
    return "跳转到了服务器内部！！！"

if __name__ == '__main__':
    app.run(debug=True)