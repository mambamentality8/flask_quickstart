#1,从flask包中导入Flask类
from flask import Flask

#2,创建对象,
#参数__name__[必填],如果是从当前模块运行的name他的值是__main__, 如果是其他模块调用运行的,那么值是模块名字
#参数static_url_path: 表示静态资源的访问地址,默认的值是, /static
#参数static_foloder: 表示静态资源的存储文件夹,默认的值是static
#参数template_folder: 表示模板文件夹,默认的值是templates
app = Flask(__name__)

print(app.static_url_path)
print(app.static_folder)


#3,使用app,绑定了路由(地址),和视图函数之间的映射关系
#视图函数,是用来返回页面的,普通的函数可以没有返回值,但是视图函数一定要有返回值
@app.route('/')
def helloworld():

    return "<h1>helloworld</h1>"


#4,判断当前文件是否是启动入口
if __name__ == '__main__':
    #5,运行服务器程序,默认的ip是127.0.0.1 默认的端口是5000
    app.run()