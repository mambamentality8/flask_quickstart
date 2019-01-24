"""
redirect配合url_for使用

- url_for使用格式: url_for(视图函数名,key=value), 返回的是一个字符串(路径)
    根据视图函数的名称,找到对应的地址


"""""
from flask import Flask,url_for,redirect

app = Flask(__name__)

#1,京东页面
@app.route('/jingdong')
def jingdong():

    # 1,使用url_for输出视图函数的地址
    # print(url_for("index_haha"))

    #2,配合redirect使用
    response = redirect(url_for("taobao",token=123))

    return response

#2,亚马逊页面
@app.route('/yamaxun')
def yamaxun():

    #1,通过redirect,url_for构建淘宝的地址
    response = redirect(url_for("taobao",token=456))

    #2,返回响应
    return response


#淘宝页面
@app.route('/taobao/<int:token>')
def taobao(token):

    #1,判断是哪里的用户
    if token == 123:
        return "欢迎京东用户,我这里什么都有,给你打9折"
    elif token == 456:
        return "欢迎亚马逊,我这里什么都有,给你打骨折"
    else:
        return "欢迎其他用户,我这里什么都有,不打折"




if __name__ == '__main__':
    app.run(debug=True)