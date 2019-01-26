import base64

import os
from flask import Flask, render_template, make_response
from flask import redirect
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        # 取到表单中提交上来的参数
        username = request.form.get("username")
        password = request.form.get("password")

        if not all([username, password]):
            print('参数错误')
        else:
            print(username, password)
            if username == 'laowang' and password == '1234':
                # 状态保持，设置用户名到cookie中表示登录成功
                response = redirect(url_for('transfer'))
                response.set_cookie('username', username)
                return response
            else:
                print('密码错误')

    return render_template('temp_login.html')


def generate_csrf():
    return bytes.decode(base64.b64encode(os.urandom(48)))

@app.route('/transfer', methods=["POST", "GET"])
def transfer():
    # 从cookie中取到用户名
    username = request.cookies.get('username', None)
    # 如果没有取到，代表没有登录
    if not username:
        return redirect(url_for('index'))

    # 没有实现跨站请求保护的转账
    # if request.method == "POST":
    #     to_account = request.form.get("to_account")
    #     money = request.form.get("money")
    #     print('假装执行转操作，将当前登录用户的钱转账到指定账户')
    #     return '转账 %s 元到 %s 成功' % (money, to_account)

    # 实现跨站请求保护的转账
    if request.method == "POST":
        to_account = request.form.get("to_account")
        money = request.form.get("money")


        # 取出表单中的 csrf_token
        form_csrf_token = request.form.get("csrf_token")
        # 取出 cookie 中的 csrf_token
        cookie_csrf_token = request.cookies.get("csrf_token")
        # 进行对比
        if cookie_csrf_token != form_csrf_token:
            return 'token校验失败，可能是非法操作'


        print('假装执行转操作，将当前登录用户的钱转账到指定账户')
        return '转账 %s 元到 %s 成功' % (money, to_account)

    csrf_token = generate_csrf()

    # 渲染转换页面
    response = make_response(render_template('temp_transfer.html', csrf_token=csrf_token))
    # 给客户端浏览器的cookie中设置csrf_token
    response.set_cookie('csrf_token', csrf_token)
    return response


if __name__ == '__main__':
    app.run(debug=True, port=9000)