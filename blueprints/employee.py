# coding:utf-8
from flask import Blueprint, render_template, jsonify, request
from common.json_responsebody import JsonResponse
import json

data = {
    "id": "1583349844145029121",
    "username": "liubang",
    "name": "汉高祖",
    "phone": "18988888888",
    "sex": "1",
    "idNumber": "320322974306010011",
    "status": 1
}
bp = Blueprint("employee", __name__, url_prefix="/employee")


@bp.route("/list", methods=['POST', 'GET'])
def get_list():
    input_data = None
    input_keys = []
    for keys in request.get_json().keys():
        input_keys.append(keys)
    print(input_keys)
    if input_keys != ['name', 'id']:
        print('键值对不对应')
        input_data = request.get_json()
        return jsonify(JsonResponse.error(msg="请校验输入body体中的输入键"))
    input_data = request.get_json()
    if request.method == 'POST':
        return jsonify(JsonResponse.success(input_data))
    else:
        return jsonify(JsonResponse.success(data=data, code=1, msg="使用get方法获取数据成功"))


@bp.route("/get", methods=['GET'])
def method_get():
    name = request.args.get("name")
    id = request.values.get("id")
    return jsonify(JsonResponse.success({"name": name, "id": id}))


@bp.route("/form/post", methods=['POST'])
def method_form_post():
    name = request.form.get("name")
    id = request.values.get("id")
    return jsonify(JsonResponse.success({"name": name, "id": id}))


@bp.route("/json/post", methods=['POST'])
def method_json_post():
    data1 = request.get_json()
    data2 = request.get_data(as_text=True)
    data3 = json.loads(data2)
    return jsonify(JsonResponse.success([data1, data2, data3]))


@bp.route("/getInfo/<int:id>", methods=['GET'])
def get_info(id):
    return jsonify(JsonResponse.success(id))


@bp.route('/index')  # 装饰器，url，路由
def index():  # 视图函数
    return render_template('index.html')
