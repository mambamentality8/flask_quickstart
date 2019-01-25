"""
自定义过滤器

- 作用: 系统提供的过滤器满足不了需求的时候自定义
- 有两种格式自定义
  - 1, 先定义函数,然后再将函数添加到系统过滤器列表中
    - def test(): pass   
    - app.add_template_filter(函数名,过滤器名字)
    - 案例: 求列表中所有元素的偶数和
    
  - 2,直接定义函数的时候,就使用装饰器进行装饰
    - @app.template_filter(过滤器名字)
    - def test():
      - pass
    - 案例: 将列表的内容反转

"""""
from flask import Flask,render_template

app = Flask(__name__)

# 1, 先定义函数,然后再将函数添加到系统过滤器列表中
def get_sum(list):
    sum = 0

    for item in list:
        if item %2 == 0:
            sum += item

    return sum

#参数1: 关联的函数名字, 参数2:在模板中使用的过滤器的名字
app.add_template_filter(get_sum,"SUM")


#2,直接定义函数的时候,就使用装饰器进行装饰
@app.template_filter("my_reverse")
def reverse_list(list):

    list.reverse()

    return list


@app.route('/')
def hello_world():

    return render_template("file04customfilter.html")

if __name__ == '__main__':
    app.run(debug=True)
