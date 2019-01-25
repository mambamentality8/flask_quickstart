"""
上下文[理解]

- 分类,共有两种
  - 1,请求上下文
    - request: 封装了每次请求中的各种参数信息
    - session: 存储着每个用户的相关信息
    
  - 2,应用上下文
    - current_app: 相当于app的代理对象,可以获取到app中的各种参数, (项目中日志信息)
    - g: 局部的变量对象,可以封装每次完整请求中的相关内容,一旦请求结束g就销毁 (项目中封装用户登陆信息)

"""""

from flask import Flask, current_app, g

app = Flask(__name__)


@app.before_request
def before_request():
    g.name = "laowang"

@app.route('/')
def hello_world():

    print(app.config.get("DEBUG"))
    print(current_app.config.get("DEBUG"))
    print(g.name)

    return "helloworld"

if __name__ == '__main__':
    app.run(debug=True)