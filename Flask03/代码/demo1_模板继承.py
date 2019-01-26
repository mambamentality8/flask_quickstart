from flask import Flask,render_template

app = Flask(__name__)
"""
模板继承：复用模板页面重复的代码块。
        *****一般用来实现复用模板页面固定不变的区域块。

继承的本质：代码替换！！！


1、把多个模板页面重复的内容，留下不动，页面特有的内容，封装成block块，让子类实现。
2、灵活运用。

补充：
1、模板不支持多继承；
2、如果既想要使用父类模板中的内容，又想要实现自己特有的内容，使用super()
3、子模板中，不能在block块之外，实现自己的代码。
4、extends语句下面所有的内容，都是复用父模板中的内容。
"""
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)