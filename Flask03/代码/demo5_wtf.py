from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
# 密钥：越复杂，session越安全，csrf更安全。
app.config['SECRET_KEY'] = 'weroxTfrA1ZXI3/QptsJmMGnuhjL+Htgrlt2eqT8H8QL1cFsnefRGQ=='

"""
wtf表单：
实现步骤：
1、导入扩展提供的表单类、字段对象、验证函数
2、自定义表单类，需要继承自wtf扩展提供的表单类
3、实例化表单类对象，传入模板
4、在模板中实现表单。

需求：注册表单，用户名、密码、确认密码、提交

wtf扩展实现的表单：
1、实现了跨站请求保护！！！
2、不仅会验证表单数据是否符合验证函数的条件
3、还会验证表单域中是否设置csrf_token!每次请求都会变化！！
4、都满足条件，返回值true，否则false

"""
# 定义表单类，实现注册表单
class Form(FlaskForm):
    wtf_user = StringField(validators=[DataRequired()])
    wtf_pswd = PasswordField(validators=[DataRequired(),EqualTo('wtf_pswd2')])
    wtf_pswd2 = PasswordField(validators=[DataRequired()])
    wtf_submit = SubmitField()


@app.route('/',methods=['GET','POST'])
def index():
    # 实例化表单类对象，传给模板
    form = Form()
    print(form.validate_on_submit())
    # 使用form.validate_on_submit()
    if form.validate_on_submit():
        # 获取表单参数,request.form.get('wtf_user')
        us = form.wtf_user.data
        ps = form.wtf_pswd.data
        ps2 = form.wtf_pswd2.data
        print(us,ps,ps2)



    return render_template('demo5_wtf.html',form=form)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)

