from flask import Flask,session
# 导入扩展包
from flask_session import Session
from redis import StrictRedis

app = Flask(__name__)
app.config['DEBUG'] = True
# 选择把session信息存储在redis数据库中
app.config['SESSION_TYPE'] = 'redis'
# 配置连接redis数据库的实例,默认本机6379，db为0号库
app.config['SESSION_REDIS'] = StrictRedis()
app.config['SESSION_USE_SIGNER'] = True # session信息签名
# 手动指定session信息的有效期
app.config['PERMANENT_SESSION_LIFETIME'] = 3600
# 配置密钥，
app.config['SECRET_KEY'] = '123'

# 把Session扩展包和程序实例关联
Session(app)

"""
状态保持session信息的存储：把session信息存储到redis中。
实现步骤：
1、导入扩展包flask_session
2、配置扩展包提供的基本信息
3、实例化Session对象

"""

@app.route('/')
def index():
    # 实现状态保持，session信息的存储
    # redis中：
    # session:8f5f0701-36f4-4fbd-84f7-b9324ad61bc7
    # 浏览器中：根据密钥生成；
    # session=8f5f0701-36f4-4fbd-84f7-b9324ad61bc7.Vin56OCGEBZI6GMKPwlDHamEt64;
    # uuid:全局唯一标识符。
    session['itcast'] = '2019'
    itcast = session.get('itcast')
    return 'hello world'

if __name__ == '__main__':


    app.run()