from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)
# 必须在mysql中手动创建数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/temp_python21'
# 设置为true或false都可以关闭警告信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
"""
数据库迁移：创建数据库表；
实现步骤：
1、导入扩展包flask_script/flask_migrate
2、实例化管理器对象
3、使用迁移框架
4、添加迁移命令给管理器
5、使用管理器执行迁移

迁移命令：
1、生成迁移仓库(文件夹)
python demo3_migrate.py db init
2、生成迁移文件(脚本)
python demo3_migrate.py db migrate -m 'init_tables'
3、执行迁移文件(创建表)
python demo3_migrate.py db upgrade
查看历史版本号：
python demo3_migrate.py db history
回退到历史版本
python demo3_migrate.py db downgrade 版本号

"""
# 创建管理器对象
manage = Manager(app)
# 使用迁移框架
# migrate = Migrate(app,db)
Migrate(app,db)
# 添加迁移命令,第一个参数表示数据库(可以自定义)，第二个参数表示迁移命令
manage.add_command('db',MigrateCommand)


class Role(db.Model):
    __tablename__ = 'roles'  # 指定表名，可以不指定，默认是同类名的表名role。
    id = db.Column(db.Integer, primary_key=True)  # 必须指定主键
    name = db.Column(db.String(32), unique=True)
    us = db.relationship('User', backref='role')

    # __repr__方法可以把查询结果的对象，显示为可读字符串。
    def __repr__(self):
        return 'role:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    mobile = db.Column(db.String(32))
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(32))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 外键，指向roles表的主键id
    phone = db.Column(db.String(64))
    # def __str__(self):
    #     return 'user:%s' % self.name
    def __repr__(self):
        return 'user:%s' % self.name


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':

    # app.run(debug=True)
    manage.run()




