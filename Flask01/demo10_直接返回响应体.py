"""
直接响应

- 1, return 响应体内容(字符串)
- 2,return 响应体,状态码
- 3,return 响应体,状态码,响应头信息

- 4,如果不想要直接返回,可以自己创建响应体对象
- response = make_response("响应体","状态码","响应头")

快速导包: alt + enter ,回车
"""""
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello_world():

    # - 1, return 响应体内容(字符串)
    # return "helloworld"

    # - 2,return 响应体,状态码
    # return "helloworld",666
    # return "helloworld","666 XIAGAO"

    # - 3,return 响应体,状态码,响应头信息
    return "helloworld","666 XIAGAO",{"Content-Type":"application/json","name":"banzhang"}


@app.route('/index')
def index():

    #1,调用make_response生成响应体对象
    response = make_response("index")

    #2,设置响应体对象属性
    response.status = "888 LUANGAO"
    response.headers["Content-Type"] = "application/json"

    #3,再返回
    return response


if __name__ == '__main__':
    app.run(debug=True)
