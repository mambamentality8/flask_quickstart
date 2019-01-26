from flask import Flask,render_template, flash,request
#导入wtf扩展的表单类
from flask_wtf import FlaskForm
#导入自定义表单需要的字段
from wtforms import SubmitField,StringField,PasswordField
#导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired,EqualTo


app = Flask(__name__)
app.config['SECRET_KEY']='SECRET_KEY'

#自定义表单类，文本字段、密码字段、提交按钮
class RegisterForm(FlaskForm):
    username = StringField("用户名：", validators=[DataRequired("请输入用户名")], render_kw={"placeholder": "请输入用户名"})
    password = PasswordField("密码：", validators=[DataRequired("请输入密码")])
    password2 = PasswordField("确认密码：", validators=[DataRequired("请输入确认密码"), EqualTo("password", "两次密码不一致")])
    submit = SubmitField("注册")

#定义根路由视图函数，生成表单对象，获取表单数据，进行表单数据验证
@app.route('/demo02', methods=["get", "post"])
def demo2():
    register_form = RegisterForm()
    # 验证表单
    if register_form.validate_on_submit():
        # 如果代码能走到这个地方，那么就代码表单中所有的数据都能验证成功
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        # 假装做注册操作
        print(username, password, password2)
        return "success"
    else:
        if request.method == "POST":
            flash("参数有误或者不完整")

    return render_template('wtf_temp_register.html', form=register_form)

if __name__ == '__main__':
    app.run(debug=True)