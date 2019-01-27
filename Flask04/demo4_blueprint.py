from flask import Flask
# 循环导包：类似于死锁，交错导入；
# 导入蓝图对象
from temp_detail import api
app = Flask(__name__)
# 注册蓝图对象,给程序实例app添加蓝图的路由
app.register_blueprint(api)

@app.route('/')
def index():
    return 'index'


@app.route('/list')
def list():
    return 'list'


if __name__ == '__main__':
    print(app.url_map)
    # 把视图函数拆分出去，可以调用，但是，不能实现路由映射。
    # from temp_detail import detail
    app.run(debug=True)
