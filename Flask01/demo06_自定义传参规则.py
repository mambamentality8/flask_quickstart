"""
自定义类型

- 需求: 接收三位整数,四位整数,手机号
- 目的:当系统提供的数据类型满足不了需求的时候需要自定义
- 格式如下:
  - 1,自定义类,继承自BaseConverter
  - 2,编写init方法,接收两个参数
  - 3,一个给父类初始化,一个给子类初始化
  - 4,将自定义的转换器,添加到系统默认的转换器列表中

"""""
from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

# - 1, 自定义类, 继承自BaseConverter
class MyRegexConverter(BaseConverter):
    #重写子类自己的规则,不能直接写死,如果写死就不够灵活了
    # regex = "\d{3}"

    # - 2, 编写init方法, 接收两个参数
    def __init__(self,map,regex):
        # - 3, 一个给父类初始化, 一个给子类初始化
        super(MyRegexConverter, self).__init__(map)
        self.regex = regex


# - 4, 将自定义的转换器, 添加到系统默认的转换器列表中
app.url_map.converters["re"] = MyRegexConverter

print(app.url_map.converters)

#1,接收三位整数
#re("\d{3}", 传递了两个参数, 一个参数(默认):app.url_map,  参数2: \d{3}
@app.route('/<re("\d{3}"):number>')
def get_three_number(number):
    return "the three number is %s"%number


#2,匹配4位整数
@app.route('/<re("\d{4}"):number>')
def get_four_number(number):

    return "the four number is %s"%number

#3,匹配手机号
@app.route("/<re('1[3-9]\d{9}'):phone>")
def get_phone_numb(phone):
    return "the phone number is %s" % phone

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
