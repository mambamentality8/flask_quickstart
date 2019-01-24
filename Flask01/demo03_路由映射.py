"""
url_map

- 作用: 用来查看当前的flask程序,关联的所有的路径
- 使用格式: app.url_map 返回的就是一个map集合,里面放着所有路由(地址)和视图函数的映射关系
- 注意点: 只有被app.url_map包含进来的视图函数才能访问

"""""

#1,到如FLask类
from flask import Flask

#2,创建Flask对象
app = Flask(__name__)

#3,使用app装饰视图函数(路由和视图函数的绑定)
#快速生成视图函数的方法: route + tab
@app.route('/haha')
def helloworld():
    return "url_map"

@app.route('/index')
def index():
    return "index"


#4,判断启动入口
#快速生成main方法,  main + tab
if __name__ == '__main__':
    #查看app中绑定了哪些路由和视图函数
    print(app.url_map)
    app.run()