from flask import Flask,render_template,redirect,url_for
# 导入扩展包
from flask_sqlalchemy import SQLAlchemy
# 导入扩展包，表单基类，验证函数、字段
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
# http://127.0.0.1:5000/?a=1&b=2#使用path转换器匹配url中的特殊字符?#&=
from werkzeug.routing import BaseConverter

app = Flask(__name__)
# 配置数据库的连接和动态追踪修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/author_book'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['SECRET_KEY'] = '0sEXJWcXTCmSk66w4rthfhp8oP4/8iY0eUUDTfDgGfAWecQBy30BDg=='
# 实例化sqlalchemy
db = SQLAlchemy(app)
# 定义模型类
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    def __repr__(self):
        return 'author:%s' % self.name

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(32))
    def __repr__(self):
        return 'book:%s' % self.info

# 自定义表单类
class Form(FlaskForm):
    wtf_auth = StringField(validators=[DataRequired()])
    wtf_book = StringField(validators=[DataRequired()])
    wtf_submit = SubmitField()


"""
需求：作者图书案例，实现的数据的增删改查
思路：
1、视图views：加载模板文件，处理请求，添加数据、删除数据、查询数据，重定向、转换器
2、模板template：渲染数据，接收视图传入的数据，基础语法、表单，wtf扩展、导包、定义表单类、实例化表单对象，csrf、secret_key；ul>li列表,a标签
3、模型model：定义模型类，作者和书籍，

实现步骤：
1、由简单到复杂，先实现基本功能，再添加新的功能
2、定义模型类，添加测试数据，传给模板，渲染数据
3、添加数据，wtf扩展表单，获取参数，提交数据到数据库
4、删除数据，模板中需要给视图传入需要删除的id；

代码需要进行异常处理：
1、IO，网络io和磁盘io；
2、对数据库的增删改查
3、转换数据类型
int('a')

"""
@app.route('/',methods=['GET','POST'])
def index():
    # 实例化表单对象
    form = Form()
    authors,books = None,None
    # 查询mysql数据库，获取作者和书籍信息
    try:
        authors = Author.query.all()
        books = Book.query.all()
    except Exception as e:
        print(e)
        # authors, books = None, None
    # 判断参数是否符合验证器的要求
    if form.validate_on_submit():
        wtf_au = form.wtf_auth.data
        wtf_bk = form.wtf_book.data
        print(wtf_au,wtf_bk)
        # 把数据添加到数据库中
        # db.session.add_all([wtf_au,wtf_bk]) # orm对象关系映射，添加数据必须通过对象,不能直接添加字符串
        auth = Author(name=wtf_au)
        bk = Book(info=wtf_bk)
        try:
            db.session.add_all([auth,bk]) # 添加数据给数据库会话对象
            db.session.commit() # 提交数据
        except Exception as e:
            print(e)
            db.session.rollback() # 提交数据发生异常，进行回滚
            return ''
        # 添加数据后，mysql中数据已经变化，需要再次查询
        try:
            authors = Author.query.all()
            books = Book.query.all()
        except Exception as e:
            print(e)

    # 把查询结果传入模板
    return render_template('demo3_author_book.html',authors=authors,books=books,form=form)

# 删除作者
# 模板页面：<a href="/del_author{{ author.id }}">删除</a>
@app.route('/del_author<int:id>')
def delete_author(id):
    # 根据id查询数据
    try:
        author = Author.query.get(id)
    except Exception as e:
        print(e)
        author = None
    # 判断如果查询到数据
    if author:
        try:
            db.session.delete(author)
            # db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
    # 重定向，redirect和url_for
    return redirect(url_for('index'))

@app.route('/del_book<int:id>')
def delete_book(id):
    # 根据id查询数据
    book = Book.query.get(id)
    # 判断如果查询到数据
    if book:
        db.session.delete(book)
        # db.session.commit()
    # 重定向，redirect和url_for
    return redirect(url_for('index'))
    pass


if __name__ == '__main__':
    # 先删除、再创建表
    db.drop_all()
    db.create_all()
    # 模拟添加数据
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    bk_xi = Book(info='吞噬星空')
    bk_xi2 = Book(info='寸芒')
    bk_qian = Book(info='飘渺之旅')
    bk_san = Book(info='冰火魔厨')
    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_xi, bk_xi2, bk_qian, bk_san])
    # 提交会话
    db.session.commit()
    app.run(debug=True)