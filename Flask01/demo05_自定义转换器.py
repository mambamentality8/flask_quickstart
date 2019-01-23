from flask import Flask
#导入基类转换器
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# 1.自定义类,继承自BaseConverter
class MyRegexConverter(BaseConverter):

    # 2.编写初始化方法, init方法, 接收两个参数, url_map, regex, 并初始化父类空间和子类空间
    def __init__(self,url_map,regex):
        super(MyRegexConverter, self).__init__(url_map)
        self.regex = regex

# 3.将自定义转换器类,添加到默认的转换列表中
app.url_map.converters['re'] = MyRegexConverter

#使用自定义转换器
#接收3位整数
@app.route('/<re("\d{3}"):num>')
def hello_world(num):

    print("num = %s"%num)

    return "the num is %s"%num

#接收一个手机号
@app.route('/<re("1[345678]\d{9}"):mobile>')
def get_phone_number(mobile):

    return "the mobile is %s"%mobile

if __name__ == '__main__':
    app.run()