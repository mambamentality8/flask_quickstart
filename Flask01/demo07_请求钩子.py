from flask import Flask
from flask import abort

app = Flask(__name__)

# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request")


# 在每次请求之前调用，这时候已经有请求了，可能在这个方法里面做请求的校验
# 如果请求的校验不成功，可以直接在此方法中进行响应，直接return之后那么就不会执行视图函数
@app.before_request
def before_request():
    print("before_request")
    # if 请求不符合条件:
    #     return "laowang"

# 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理
@app.after_request
def after_request(response):
    print("after_request")
    response.headers["Content-Type"] = "application/json"
    return response

# 请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息(这里错误是硬件撑不住了)
@app.teardown_request
def teardown_request(e):
    print("teardown_request")

@app.route('/')
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)