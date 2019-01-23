from flask import Flask,abort
from flask import redirect

app = Flask(__name__)

class Config(object):
    DEBUG = True

app.config.from_pyfile('./config.ini')

@app.route('/game/<int:age>')
def play_game(age):
    #异常抛出
    abort(404)

    return "helloworld"

#异常捕获
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return redirect ('http://hd.mi.com/webfile/zt/hd/2014042802/cn.html')

if __name__ == '__main__':
    app.run()