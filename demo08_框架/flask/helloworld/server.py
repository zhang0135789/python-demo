from flask import Flask, request

app = Flask(__name__, static_folder = "path1", template_folder="path2")

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

if __name__ == "__main__":
    # 配置ip和端口号
    app.run(host='0.0.0.0', port=8080, debug=True)