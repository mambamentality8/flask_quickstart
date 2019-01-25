"""
状态保持

- 作用: 用来记录服务器和浏览器的交互记录
- 实现状态保持有两种方式:
  - cookie
    - 作用: 用来保持服务器和浏览器的交互数据,由服务器设置,存储在浏览器的
    - 场景: 广告推送
    - 设置方式: response.set_cookie(key,value,max_age)
      - max_age:有效期单位是秒
    - 获取方式
      - value = request.cookies["key"]

"""""
from flask import Flask, make_response, request

app = Flask(__name__)

#1,浏览电脑信息
@app.route('/computer')
def computer():

    #1,创建响应体对象
    response = make_response("浏览了电脑页面")

    #2,设置cookie
    response.set_cookie("computer","lenovo")
    response.set_cookie("address","beijing",5)

    #3,返回响应
    return response

#2,浏览了鞋子信息
@app.route("/shoes")
def shoes():
    #1,获取cookie信息
    # name = request.cookies["computer"]
    # name2 = request.cookies["address"]

    #建议使用get方式获取,获取不到返回的是None
    name = request.cookies.get("computer")
    name2 = request.cookies.get("address")

    #2,返回响应
    return "访问了鞋子,我推荐了 %s, %s"%(name,name2)


if __name__ == '__main__':
    app.run(debug=True)
