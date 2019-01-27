from flask import Flask,jsonify
from werkzeug.routing import BaseConverter
from config import config_dict

import json

# json字符串 = json.dumps(字典)
# 字典 = json.loads(json)
# f = open()
# f = 'a'
# json.dump()# 操作的是文件对象
# json.load()# 操作的是文件对象

app = Flask(__name__)
app.config.from_object(config_dict['pro'])

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    app.run()