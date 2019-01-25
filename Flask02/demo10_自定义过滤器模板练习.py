from flask import Flask,render_template

app = Flask(__name__)

#自定义过滤器实现颜色过滤
@app.template_filter("my_filter")
def my_filter(index):
    if index == 1:
        return "yellow"
    elif index ==2:
        return "green"
    elif index ==3:
        return "red"
    else:
        return "purple"


@app.route('/')
def hello_world():

    # 1, 定义数据
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]

    # 2, 携带数据渲染模板
    return render_template("file06practice_filter.html",my_list=my_list)

if __name__ == '__main__':
    app.run(debug=True)