"""
,jinja2中的模板语法

- 1, 获取变量的值, {{ 变量 }}

- 2, 分支语句if:
      {% if 条件 %}
      
      {%else %}
      
      {% endif %}
      
- 3,for循环语句
      {% for 变量 in 容器%}
      
      {% endfor %}
  
- 4,注释
    {# 注释的内容 #}
"""""

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():

    #1.定义各种类型的变量
    age = 10
    name = "zhangsan"
    tuple = (1,2,3,4,5)
    list = [6,7,8,9,10]
    dict = {
        "name":"老王",
        "age":"33",
        "sex":"man"
    }

    #2,携带数据,渲染页面
    return render_template("file02template_program.html",age=age,name=name,tuple=tuple,list=list,dict=dict)

if __name__ == '__main__':
    app.run(debug=True)
