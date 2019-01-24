from flask import Flask, make_response, request

app = Flask(__name__)

#设置cookie值
@app.route('/set_cookie')
def set_cookie():

    response = make_response("set cookie")
    response.set_cookie("name","zhangsan")
    response.set_cookie("age","13",10) #10秒有效期

    return response

#获取cookie
@app.route('/get_cookie')
def get_cookie():

    #获取cookie,可以根据cookie的内容来推荐商品信息
    # name = request.cookies['haha']
    name = request.cookies.get('name')
    age = request.cookies.get('age')

    return "获取cookie,name is %s, age is %s"%(name,age)

if __name__ == '__main__':
    app.run(debug=True)