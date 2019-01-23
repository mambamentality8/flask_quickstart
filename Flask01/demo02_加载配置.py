#1.导入Flask类
from flask import Flask

#2.创建Flask对象接收一个参数__name__，它会指向程序所在的包
app = Flask(__name__)

# 配置对象，里面定义需要给 APP 添加的一系列配置
class Config(object):
    DEBUG = True

# 从配置对象中加载配置
#app.config.from_object(Config)

# 从配置文件中加载配置
app.config.from_pyfile('./config.ini')
# 加载指定环境变量名称所对应的相关配置
#app.config.from_envvar('FLASKCONFIG')

#3.装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    return 'Hello World'

#4.Flask应用程序实例的run方法,启动WEB服务器
if __name__ == '__main__':
    app.run()