"""
jinja2过滤器

- jinja2中提供了两种常见的过滤器
  - 1,字符串过流程
    - 格式: {{字符串 | 过滤器}}
    - 常见的字符串过滤器有:
      - upper: 将字符串转大写
      - lower: 将字符串转小写
      - title: 将字符串首字母转大写,其他字符小写
      - ....
  - 2,列表过滤器
    - 格式: {{列表 | 过滤器}}
    - 常见的过滤器过滤器有:
      - sum: 获取列表中所有元素的和
      - first: 获取列表第一个元素
      - last: 最后一个元素
      - ....

"""""
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template("file03filter.html")

if __name__ == '__main__':
    app.run(debug=True)