"""
- ,flask-script
- 作用: 
  - 1,属于flask中的扩展,需要安装才能使用,通过脚本的方式就可以启动程序(可以指定参数)
  - 2,可以和flask_migrate配合做数据库的迁移操作
- 使用流程:
  - 1,安装扩展包
    - pip install flask-script
    
  - 2,导入flask-script中的管理类
    - from flask_script import Manager
    
  - 3,创建Manager对象,传入app参数
    - manager = Manager(app)
    
  - 4,启动程序
    - manager.run()
    
  - 脚本运行方式
    - python xxx.py runserver -h 地址 -p 端口 -d

"""""
from flask import Flask
from flask_script import Manager

app = Flask(__name__)
app.config["DEBUG"] = True

#创建Manager对象,传入app参数
manager = Manager(app)

@app.route('/')
def hello_world():

    return "helloworld"

if __name__ == '__main__':
    manager.run()