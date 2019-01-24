"""
app.run()

- 运行服务器程序,有如下默认参数
- host地址: 127.0.0.1(localhost)
- port端口: 5000
- debug: 默认值是False
  - 建议在开发阶段设置为True
  - 好处:
    - 1,代码变动之后(ctrl+s),自动部署
    - 2,如果程序报错了,有友好提示

"""""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():

    # 1/0

    return "<h1>helloworld</h1>"

if __name__ == '__main__':
    #默认ip是127.0.0.1, 默认端口是5000,默认debug是False
    app.run(port=5001,debug=True)
