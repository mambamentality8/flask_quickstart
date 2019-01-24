"""
abort,errorhandler

- 作用: 用来处理自定义的错误信息
- abort格式: abort(异常代码)
- @app.errorhandler(异常代码)

"""""
from flask import Flask, redirect, abort

app = Flask(__name__)

@app.route('/play_game/<int:age>')
def play_game(age):

    #判断年龄
    if age < 18:
        abort(403)

    return "<h1 style='color:red;'>可以玩游戏</h1>"

#处理404异常页面,只能捕捉指定的
@app.errorhandler(404)
def page_not_found(e):

    # return "服务器搬家了 %s"%e
    return redirect("http://hd.mi.com/webfile/zt/hd/2014042802/cn.html")


#处理403页面异常,只能捕捉指定的
@app.errorhandler(403)
def no_pass(e):
    print(e)
    return "你的年龄太小了,不能玩游戏"



if __name__ == '__main__':
    app.run()
