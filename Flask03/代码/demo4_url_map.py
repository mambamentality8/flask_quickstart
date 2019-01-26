from flask import Flask,render_template
from werkzeug.routing import MapAdapter,Map
from werkzeug.wrappers import Response

app = Flask(__name__)

"""
装饰器路由的实现：
1、Rule：路由规则，<>对象，容器，存储每个url路径/请求方法和端点(视图函数名)的对应关系。
rule = self.url_rule_class(rule, methods=methods, **options)
<Rule '/123' (HEAD, OPTIONS, GET) -> index>
http请求方法：get(查询)、post(增加)、put(修改)、delete(删除)

2、Map：路由映射，[]列表,存储所有的Rule类规则；

3、MapAdapter：负责匹配，正则匹配，满足一个url的规则，并且满足请求方法，调用对应的视图函数(端点)。

Flask类传入的参数，表示模块名，__name__
1、默认传入__name__，框架默认创建静态路由和模板文件，方便静态文件的访问，和模板文件夹的访问
2、如果传入标准模块名，找不到当前文件所在的位置，会影响静态文件和模板文件的访问；
3、如果传入任意字符串，都不会影响视图、模板、静态文件的访问。因为这个时候的实例路径都是当前文件所在的位置


补充：
url可以重复，因为不同的http请求方法，是对服务器不同的操作；
视图函数不能重复！

路由映射列表：从上往下，依次匹配，首先匹配path，其次匹配请求方法，如果找到，不会继续查找。
1、列表根据索引存储数据，数据可以重复。
2、字典key值不能重复。

"""

"""
flask中返回数据类型
1.字符串
2.json数据
3.重定向
4.元组
"""


@app.route('/')
def index2018():
    # return 'index'
    # 不能返回字典
    # my_dict = {'itcast':'python21'}
    # 不能返回列表
    # my_list = [1,2,3,4]
    # return my_list
    # 能不能返回元组,可以返回字符串和元组
    # 作业：元组中除了能返回字符串，还能返回什么？？
    return ('hello world',)

@app.route("/abc")
@app.route('/123')
def index2019():
    return 'index 2019'
    # a,b = 1,2
    # return a,b

# 不使用装饰器，手动添加路由映射
# app.add_url_rule('/','index',index)

if __name__ == '__main__':
    # 查看路由映射
    print(app.url_map)
    app.run(debug=True)


