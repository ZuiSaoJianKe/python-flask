# coding:utf-8
from flask import Blueprint, render_template, jsonify, request, session
from common.json_responsebody import JsonResponse
from .models import *
from random import randint
import json
from flask_mail import Message
import pickle

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


@bp.route('/test/list')
def test_list():
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


@bp.route('/redisSet', methods=['GET', 'POST'])
def redis_set():
    name = 'mink'
    fds.set(name, 'mike')
    # rds.set(name,'mike'.encode())
    # print('mike'.encode())
    redis_data = rds.get('mink')
    print(redis_data)
    return jsonify(JsonResponse.success(data={name: redis_data.decode()}, msg='添加并且查询redis成功'))


@bp.route('/mongoAdd', methods=['POST'])
def add_emp():
    data = request.get_json()
    input_keys = []
    for keys in request.get_json().keys():
        input_keys.append(keys)
    if input_keys != ['name']:
        return jsonify(JsonResponse.error(msg="请校验body体中的输入键"))
    employees = Employee.objects().all()
    print(len(employees))
    emp = Employee(name=data['name'])
    emp.save()
    return jsonify(JsonResponse.success(msg="mongo添加员工成功"))


'''
下方实战接口
'''


@bp.route('/regist', methods=['POST'])
def regist():
    data = request.get_json()
    input_keys = []
    for keys in request.get_json().keys():
        input_keys.append(keys)
    if input_keys != ['name', 'password', 'mail']:
        return jsonify(JsonResponse.error(msg="请校验body体中的输入键"))
    employee = EmployeeModel.query.filter(EmployeeModel.name == data['name']).first()
    if employee is not None:
        return jsonify(JsonResponse.error(msg="用户名已存在"))
    mail = EmployeeModel.query.filter(EmployeeModel.mail == data['mail']).first()
    if mail is not None:
        return jsonify(JsonResponse.error(msg="号码已经使用"))
    else:
        emp = EmployeeModel(name=data['name'], pswd=data['password'], mail=data['mail'])
        db.session.add(emp)
        db.session.commit()
        employee = EmployeeModel.query.filter(EmployeeModel.name == data['name']).first()
        del (employee.__dict__)['_sa_instance_state']
        return jsonify(JsonResponse.success(msg="注册成功", data=(employee.__dict__['create_time'])))


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    input_keys = []
    for keys in request.get_json().keys():
        input_keys.append(keys)
    if input_keys != ['name', 'password', 'code']:
        return jsonify(JsonResponse.error(msg="请校验body体中的输入键"))
    employee = EmployeeModel.query.filter(EmployeeModel.name == data['name']).first()
    # del (employee.__dict__)['_sa_instance_state']
    # # print(type(employee.__dict__))
    if employee is None:
        return jsonify(JsonResponse.error(msg="用户不存在"))
    elif data['password'] != EmployeeModel.query.filter(EmployeeModel.name.like(data['name'])).all()[0].pswd:
        return jsonify(JsonResponse.error(msg="密码错误"))
    check_code = fds.get(data['name'])
    # print(check_code)
    if check_code is None:
        return jsonify(JsonResponse.error(msg="登陆失败，验证码已失效，请重新发送验证码"))
    else:
        if data['code'] != check_code.decode():
            return jsonify(JsonResponse.error(msg='验证码错误'))
        else:
            # (employee.__dict__).pop('_sa_instance_state')
            del (employee.__dict__)['_sa_instance_state']
            del (employee.__dict__)['create_time']
            del (employee.__dict__)['update_time']
            del (employee.__dict__)['pswd']
            session['emp_id'] = (employee.__dict__)['id']
            print(f'登陆接口获得session为{session}')
            del (employee.__dict__)['id']
            return jsonify(JsonResponse.success(msg=f"登录成功,sessionid is {session.get('emp_id')}", data=(employee.__dict__)))

@bp.route('/logout',methods=['POST'])
def logout():
    session.clear()
    print(f"logout的方法session为{session}")
    return jsonify(JsonResponse.success(msg="退出登陆成功"))

@bp.route("/list")
def get_list():
    print(session)
    print(session.get('emp_id'))
    page = request.args.get("page")
    page_size = request.args.get("pageSize")
    if page_size is None:
        page_size = 10
    if page is not None:
        offset = (int(page) - 1) * int(page_size)
    else:
        offset = 0
    key_word = request.args.get('name')
    if key_word is None:
        employees = EmployeeModel.query.offset(offset).limit(page_size).all()
    else:
        employees = EmployeeModel.query.filter(EmployeeModel.name.like('%' + key_word + '%')).offset(offset).limit(
            page_size).all()
    list_emp = []
    for employee in employees:
        del (employee.__dict__)['_sa_instance_state']
        del (employee.__dict__)['create_time']
        del (employee.__dict__)['update_time']
        del (employee.__dict__)['id']
        del (employee.__dict__)['pswd']
        list_emp.append(employee.__dict__)
    return jsonify(JsonResponse.success(data=list_emp, msg='查询成功'))


@bp.route('/sendCode', methods=['POST'])
def send_code():
    code_list = []
    for i in range(6):
        code_list.append(str(randint(0, 9)))
    # code = [str(randint(0, 9)) for i in range(6)]
    code = ''.join(code_list)
    emp_name = request.get_json()['name']
    # 获取员工的信息，如果不为空，redis存入缓存，且发送验证码
    emp = EmployeeModel.query.filter(EmployeeModel.name == emp_name).first()
    if emp is not None:
        try:
            fds.set(emp_name, code)
            fds.expire(emp_name, 3600)
            emp_mail = (emp.__dict__)['mail']
            msg = Message('flask验证码测试', sender='alphonse9317@163.com', recipients=[emp_mail])
            msg.body = code
            mail.send(msg)
            return jsonify(JsonResponse.success(msg='发送验证码成功'))
        except Exception as e:
            return jsonify(JsonResponse.success(msg='异常情况，发送验证码可能失败'))
    else:
        return jsonify(JsonResponse.error(msg='员工不存在'))

