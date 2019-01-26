from flask import Flask,render_template

app = Flask(__name__)
"""
包含：
概念：完整复用模板页面的代码。
实现：关键字include：

备注：
建议加上关键字ignore missing，在包含的文件不存在或找不到时，不会报错。

总结：
继承：block/extends,本质是代码替换，一般用来复用模板页面固定不变的代码块。
宏：macro，本质是函数，一般用来复用模板页面动态的功能代码。
包含：include，本质是复制，一般用来实现html页面的完整复用。

"""


@app.route('/')
def index():
    return render_template('demo3_include.html')

if __name__ == '__main__':
    app.run(debug=True)