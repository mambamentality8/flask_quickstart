from flask import Flask
#1.从flask_script中导入Manager类
from flask_script import Manager

app = Flask(__name__)

# 2.使用Manager管理app对象
manager = Manager(app)

@app.route('/')
def hello_world():
    return "helloworld"

if __name__ == '__main__':
    manager.run()