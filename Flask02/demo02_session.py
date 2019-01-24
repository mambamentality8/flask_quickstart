from flask import Flask,session

app = Flask(__name__)

#设置SECRET_KEY
app.config["SECRET_KEY"] = "fhdk^fk#djefkj&*&*&"

#设置session
@app.route('/set_session/<path:name>')
def set_session(name):

    session["name"] = name
    session["age"] = "13"

    return "set session"

#获取session内容
@app.route('/get_session')
def get_session():

    name = session.get('name')
    age = session.get('age')

    return "name is %s, age is %s"%(name,age)

if __name__ == '__main__':
    app.run(debug=True)