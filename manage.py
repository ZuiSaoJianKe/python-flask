# coding:utf-8
from RealProject import create_app
from flask import session, g, jsonify, request
from common.json_responsebody import JsonResponse
# from app.employee.models import EmployeeModel

app = create_app()


@app.before_request
def bf_request():
    all_path_list = [
        '/employee/login',
        '/employee/regist',
        '/employee/sendCode',
        '/employee/mongoAdd',
        '/employee/test/list',
        '/employee/get',
        '/employee/form/post',
        '/employee/json/post',
        '/employee/getInfo/<int:id>',
        '/employee/index',
        '/employee/redisSet',
        '/employee/mongoAdd',
        '/employee/list',
        '/employee/logout'
    ]
    allow_path_list = [
        '/employee/login',
        '/employee/regist',
        '/employee/sendCode'
    ]
    print(request.path)
    empid = session.get('emp_id')
    print(empid)
    print(f'过滤器获得的session为{session}')
    if request.path not in all_path_list:
        return jsonify(JsonResponse.error('接口并不存在'))
    if empid is None and request.path not in allow_path_list:
        return jsonify(JsonResponse.error(msg='未登录'))




if __name__ == '__main__':
    app.run(debug=True)
