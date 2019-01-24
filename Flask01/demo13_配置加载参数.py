"""
1, 从配置对象中加载(常用)
    app.config.from_object()
    
2,从配置文件中加载
    app.config.from_pyfile()
    
3, 从环境变量中加载(了解)
    app.config.from_envvar()

app.config: 里面表示了app应用运行的所有环境

"""""

from flask import Flask

app = Flask(__name__)

# 不建议直接设置,不好管理
# print(app.config)
# app.config['DEBUG'] = True

# 1, 从配置对象中加载(常用)
class MyConfig(object):
    #设置调试模式
    DEBUG = True

    #mysql的值配置

    #redis的配置

    #....

app.config.from_object(MyConfig)

# 2,从配置文件中加载
# app.config.from_pyfile("config.ini")

# 3, 从环境变量中加载(了解)
# app.config.from_envvar("HAHAHA")

@app.route('/')
def hello_world():

    return "helloworld"


if __name__ == '__main__':
    app.run()