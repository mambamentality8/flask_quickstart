from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 必须在mysql中手动创建数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/python21'
# 设置为true或false都可以关闭警告信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 展示sql语句
# app.config['SQLALCHEMY_ECHO'] = True

"""
数据库的基本操作：
1、准备工作的实现步骤：
1.1导入扩展包flask_sqlalchemy
1.2指定连接的数据库，手动创建数据库
1.3配置动态追踪修改信息的关闭
1.4实例化SQLAlchemy对象，必须传入app程序实例
1.5定义模型
     
2、模型类的定义步骤：
2.1定义类，必须继承自db.Model
2.2定义字段，Column()
2.3定义关系引用，relationship()

3、需求：定义两个模型类，
角色：一方，管理员和普通用户；
用户：多方，具体的用户数据，张三、李四、王五等等

"""
# 实例化sqlalchemy对象
db = SQLAlchemy(app)
# db.init_app(app)
"""
工厂函数：函数的作用创建app，可以给工厂函数传入参数，可以根据参数的不同，生成不同环境下的app。
def create_app(debug_name):
    app = Flask(__name__)
    app.config.from_object(debug_name)
    db.init_app(app)
    return app

"""


class Role(db.Model):
    __tablename__ = 'roles'  # 指定表名，可以不指定，默认是同类名的表名role。
    id = db.Column(db.Integer, primary_key=True)  # 必须指定主键
    name = db.Column(db.String(32), unique=True)
    # 关系引用的定义，
    # 1、一对多关系中，一方定义关系，多方定义外键
    # 2、第一个参数：另外一方的类名，第二个参数backref：反向引用，给另外一方添加一个属性；
    # 3、us可以实现一对多的查询，role可以实现多对一的查询
    # 4、关系引用在数据库中没有实体字段
    us = db.relationship('User', backref='role')

    # __repr__方法可以把查询结果的对象，显示为可读字符串。
    def __repr__(self):
        return 'role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 外键，指向roles表的主键id

    # def __str__(self):
    #     return 'user:%s' % self.name
    def __repr__(self):
        return 'user:%s' % self.name


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    # 删除表
    db.drop_all()
    # 创建表
    db.create_all()
    # 模拟添加数据,添加数据必须通过模型
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    # session：表示数据库会话对象，封装了对数据库的基本操作rollback/commit/delete，add_all表示添加多条数据，add添加一条数据
    db.session.add_all([ro1, ro2])
    db.session.commit()  # 提交数据到mysql数据库
    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()
    app.run(debug=True)

"""
在此模块下打开终端进入交互模式
In [1]: from demo1_query import *

In [2]: Role.query.all()

基本查询：
1、查询所有数据；
>>> Role.query.all()
[<Role 1>, <Role 2>]
>>> User.query.all()
[<User 1>, <User 2>, <User 3>, <User 4>]
2、查询第一个数据：
>>> User.query.first()
user:wang
3、get查询，参数为主键
>>> User.query.get(1)
user:wang
>>> User.query.get(2)
user:zhang
过滤查询：
1、filter查询，参数可以不传入参数，默认查询所有数据，如果传入参数必须使用类名.字段，后面必须执行器
>>> User.query.filter().all() 返回列表
[user:wang, user:zhang, user:chen, user:zhou]
filter_by查询，参数只能使用字段名，只能使用等值，赋值操作。
>>> User.query.filter_by(id>=1).all()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>=' not supported between instances of 'builtin_function_or_method' and 'int'
>>> User.query.filter_by(User.id=1).first()
  File "<stdin>", line 1
SyntaxError: keyword can't be an expression
>>> User.query.filter_by(id=1).first()
user:wang

2、比较运算
>>> User.query.filter(User.id<=1).all()
[user:wang]
>>> User.query.filter().first() 返回一个
user:wang
3、使用字符串判断
>>> User.query.filter(User.name.startswith('z')).all()
[user:zhang, user:zhou]
3、多个条件查询,默认是and关系
>>> User.query.filter(User.name.startswith('w'),User.email.endswith('163.com')).all()
[user:wang]
4、逻辑运算符，必须导入使用from sqlalchemy import not_/and_/or_
>>> User.query.filter(and_(User.name.startswith('w'),User.email.endswith('163.com'))).all()
[user:wang]
>>> User.query.filter(or_(User.name.startswith('w'),User.email.endswith('163.com'))).all()
[user:wang, user:zhou]
>>> User.query.filter(or_(User.name=='wang',User.email.endswith('163.com'))).all()
[user:wang, user:zhou]
>>> User.query.filter(or_(User.name!='wang',User.email.endswith('163.com'))).all()
[user:wang, user:zhang, user:chen, user:zhou]
5、排序查询:desc表示倒序排序，asc表示升序排序
>>> User.query.filter().order_by(User.id.desc()).all()
[user:zhou, user:chen, user:zhang, user:wang]
>>> User.query.filter().order_by(User.id.asc()).all()
[user:wang, user:zhang, user:chen, user:zhou]

6、分页查询:
paginate，查询返回的结果为分页对象，分页对象.items、分页对象.pages、分页对象.page
三个参数;
第一个表示当前页数，
第二个表示每页数据条目数，
第三个参数表示分页异常报错信息，False表示不报错，True表示报错
>>> page = User.query.filter().paginate(1,2,False)
>>> page.items 表示获取分页后的数据
[user:wang, user:zhang]
>>> page.pages 表示获取分页后的总页数
2
>>> page.page 表示获取分页后的当前页数
1
7、修改数据：update
>>> User.query.filter(User.name=='zhang').update({'name':"yang"})
1
>>> db.session.commit()
7.1修改后提交数据，建议使用db.session.add(一个对象)/add_all([多个对象])
    不建议直接使用commit，因为commit会把所有对象的修改一次性全部提交，如果只需要修改一个数据，
    手动添加一个对象给db.session数据库会话对象。
>>> user = User.query.filter(User.name=='yang').first()
>>> user.name == 'zhang'
False
>>> user.name = 'zhang'
>>> User.query.all()
[user:wang, user:zhang, user:chen, user:zhou]
>>> db.session.add(user)
>>> db.session.commit()

8、一对多的查询:首先获取一方的对象，然后调用relationship返回的对象，一方对象.us
>>> Role.query.get(1)
role:admin
>>> Role.query.get(1).us
>>> role = Role.query.get(1)
>>> role.us
[user:wang, user:zhou]

9、多对一的查询:首先获取多方的对象，然后调用backref定义的字符串，多方对象.role
>>> User.query.get(2)
user:zhang
>>> u = User.query.get(2)
>>> u.role
role:user


"""
