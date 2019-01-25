"""
session

- 作用: 用来保持服务器和客户端交互的数据(敏感数据),由服务器设置,存储在服务器
- 场景: 用来做用户的登陆状态保持
- 设置方式:
  - session["key"]  = value
- 获取方式:
  - value = session.get("key")

"""""
from flask import Flask, session

app = Flask(__name__)
#用来给sessionid加密的
app.config["SECRET_KEY"] = "fkdkfdjkfdkfjkdjfkd"

#1,用户登陆了
@app.route('/login/<path:name>')
def login(name):

    #1,设置session
    session["name"] = name

    #2,返回响应
    return "欢迎%s来到python21网"%name

#2,购物页面
@app.route('/shopping')
def shopping():

    #1,获取session信息
    name = session.get("name")

    #2,返回响应
    if name:
        return "欢迎%s再次回来购物"%name
    else:
        return "登陆后再来购物"


if __name__ == '__main__':
    app.run(debug=True)
