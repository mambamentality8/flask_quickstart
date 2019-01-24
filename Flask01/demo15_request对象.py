from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def hello_world():

    #1,获取的是非表单提交的post的数据
    # print(request.data)

    #2,request.form: 获取的是表单提交的post的数据
    # print(request.form)

    # 3,request.args: 获取的是地址中,问号后面拼接的参数,比如:www.baidu.com?name=zhangsan&age=13
    # print(request.args)

    #4,request.method: 获取的是请求方式
    # print(request.method)

    #5,request.url: 获取的是请求的地址
    print(request.url)

    return "helloworld"


if __name__ == '__main__':
    app.run(debug=True)