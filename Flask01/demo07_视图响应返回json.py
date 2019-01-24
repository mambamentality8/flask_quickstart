"""
视图函数响应

- 共有三种形式
- 1,返回json数据
  - 使用,jsonify,生成json数据响应体
  - 格式: jsonify(dict)
  - 简化格式: jsonify(key1=value1,key2=value2,...)

"""""
from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():

    #0,定义字典
    dict = {
        "name":"zhangsan",
        "age":13
    }

    #1,调用jsonify生成json数据
    response = jsonify(dict)

    #2,返回数据
    # return response

    #简化格式
    return jsonify(name="laowang",age=23,sex="man")

if __name__ == '__main__':
    app.run(debug=True)