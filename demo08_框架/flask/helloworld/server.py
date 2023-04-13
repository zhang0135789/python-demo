from flask import Flask, request

'''
1.2.Flask的配置
    python内置变量__name__的值是字符串__main__ 。Flask类将这个参数作为程序名称。当然这个是可以自定义的，比如app = Flask("my-app")。
    Flask默认使用static目录存放静态资源，templates目录存放模板，这是可以通过设置参数更改的：
'''
app = Flask(__name__, static_folder = "static", template_folder="templates")

'''
1.1.返回一个hello world
'''
@app.route('/')
def hello_world():
    print(request.path)
    print(request.full_path)
    print(request.args.__str__())
    # 获取url中的参数
    print(request.args.get("p"))
    # 获取url中的同名参数
    print(request.args.getlist("p"))
    return "helloworld"

'''
测试：
    curl -H "Content-Type: application/json" -X POST -d '{"user_id": "123", "coin":100, "success":1, "msg":"OK!" }' http://localhost:8080/register
'''
@app.route('/register', methods=['POST'])
def register():
    print("request headers: ", request.headers)
    print("request stream: ", request.stream.read())
    return 'welcome'

'''
1.3.debug调试模式
    将debug设置为True的另一个好处是，程序启动后，会自动检测源码是否发生变化，若有变化则自动重启程序。这可以帮我们省下很多时间。
1.4.绑定ip和端口
'''
if __name__ == "__main__":
    # 配置ip和端口号
    app.run(host='0.0.0.0', port=8080, debug=True)



