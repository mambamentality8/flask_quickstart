"""
请求钩子

- 目的: 知道不同请求钩子的执行顺序
- flask中提供的请求钩子有四种:
  - 1, before_first_request:在处理第一个请求前执行
  - 2,before_request:在每次请求前执行,在该装饰函数中,一旦return,视图函数不再执行
  - 3, after_request:如果没有抛出错误，在每次请求后执行
    	接受一个参数：视图函数作出的响应
    	在此函数中可以对响应值,在返回之前做最后一步处理,再返回
  - 4, teardown_request：在每次请求后执行,接受一个参数:用来接收错误信息
    

"""""
from flask import Flask, make_response

app = Flask(__name__)

# 1, before_first_request:在处理第一个请求前执行,适合做:建立数据库连接
@app.before_first_request
def before_first_request():
    print("before_first_request")

# 2, before_request:每次请求前都会执行,适合做:参数的校验
@app.before_request
def before_request():
    print("before_request")
    # return "参数校验不通过,你不能访问"

# 3, after_request:每次在视图函数执行完成之后,再执行, 适合做,对数据的交互格式做统一处理
@app.after_request
def after_request(resp): #resp是视图函数返回的结果
    print("after_request")
    #设置返回的数据为json格式
    resp.headers["Content-Type"] = "application/json"
    # resp.data = "hahahahaha"
    return resp

# 4, teardown_request: 每次请求结束之后执行,适合做,对异常信息进行记录
# 这里的异常:不是指程序的异常信息
@app.teardown_request
def teardown_request(e):
    print(e)
    print("teardown_request")


@app.route('/')
def hello_world():
    print("这是支付页面")
    return "this is pay page"


if __name__ == '__main__':
    app.run(debug=True)
