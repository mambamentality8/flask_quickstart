from flask import Flask
from flask import flash
from flask import render_template
from flask import request

app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'

@app.route('/demo01', methods=["get", "post"])
# 提交表单进入的函数
def demo1():
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            flash("参数不足")
        elif password != password2:
            flash("两次密码不一致")
        else:
            # 假装做注册操作
            print(username, password, password2)
            return "success"

    # 第一次请求进入表单页面
    return render_template('my_temp_register.html')


if __name__ == '__main__':
    app.run(debug=True)
