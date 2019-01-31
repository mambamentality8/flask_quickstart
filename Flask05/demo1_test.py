import unittest
from demo3_author_book import *
"""
需求：测试数据库；
    往demo3_author_book文件中的模型中插入数据；
单元测试实现步骤：
1、导入测试模块
2、定义测试类，必须继承自单元测试的类
3、定义setUp方法和tearDown方法；
4、定义测试方法,函数名必须以test开头。

"""
class DatabaseTest(unittest.TestCase):

    # 方法名为固定的，作用类似于初始化函数，会首先执行，用来做测试前的准备工作；指定连接的数据库、创建数据、构造客户端等
    def setUp(self):
        # 指定连接的数据库
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/temp_test'
        # 创建数据库表
        db.create_all()

    # 方法名为固定的，作用类似于析构函数__del__，会最后执行，用来做测试后的扫尾构造；清除测试数据等；
    def tearDown(self):
        # 表示移除数据库会话对象
        db.session.remove()
        db.drop_all()


    # 测试函数的函数名必须以test开头；
    def test_add_data(self):
        # 模拟添加数据
        author = Author(name='itcast')
        book = Book(info='python')
        db.session.add_all([author,book])
        db.session.commit()
        # 提交后查询数据提交是否成功
        auth = Author.query.filter(Author.name=='itcast').first()
        bk = Book.query.filter_by(info='python').first()
        # 断言数据存在
        self.assertIsNotNone(auth)
        self.assertIsNotNone(bk)
        pass

