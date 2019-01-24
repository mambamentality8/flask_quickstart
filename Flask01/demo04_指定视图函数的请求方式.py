"""
指定视图函数的请求方式

- 格式: @app.route('路径',methods=["请求方式1","请求方式2",...])
- 常见的请求方式:
  - GET,POST
  - DELETE,PUT
- 注意点:
  - 如果不指定请求方式,默认就是get请求

"""""

#1,从flask中导入Flask类
from flask import Flask


#2,创建Flask对象
app = Flask(__name__)


#3,使用flask对象,绑定路由和视图函数
@app.route('/index',methods=["POST","GET"])
def index():

    return "this is index"


#4,判断启动入口
if __name__ == '__main__':
    print(app.url_map)
    app.run()