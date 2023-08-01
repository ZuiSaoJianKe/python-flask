# coding:utf-8
from RealProject import create_app
from flask import session, g, jsonify, request
from common.json_responsebody import JsonResponse
from app.employee.models import EmployeeModel

app = create_app()


# @app.before_request
# def bf_request():
#     all_path_list = [
#         '/employee/login',
#         '/employee/regist',
#         '/employee/sendCode',
#         '/employee/mongoAdd',
#         '/employee/test/list',
#         '/employee/get',
#         '/employee/form/post',
#         '/employee/json/post',
#         '/employee/getInfo/<int:id>',
#         '/employee/index',
#         '/employee/redisSet',
#         '/employee/mongoAdd',
#         '/employee/list',
#         '/employee/logout'
#     ]
#     path_list = [
#         '/employee/login',
#         '/employee/regist',
#         '/employee/sendCode'
#     ]
#     print(request.path)
#     empid = session.get('emp_id')
#     if request.path in all_path_list:
#         if empid is not None:
#             emp=EmployeeModel.query.fillter(empid)
#             pass
#         else:
#             if request.path in path_list:
#                 pass
#             else:
#                 print(empid)
#                 return jsonify(JsonResponse.error(msg='未登录',data=empid))
#     else:
#         return jsonify(JsonResponse.error(msg='接口不存在'))



if __name__ == '__main__':
    app.run(debug=True)
