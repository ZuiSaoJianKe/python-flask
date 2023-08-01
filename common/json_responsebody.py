# coding:utf-8
class JsonResponse():
    def __init__(self, data, code, msg):
        self.data = data
        self.code = code
        self.msg = msg

    @classmethod
    def success(cls, data=None, code=0, msg='success'):
        # print(type(cls(data, code, msg)))
        return cls(data, code, msg).__dict__

    @classmethod
    def error(cls, data=None, code=-1, msg='error'):
        return cls(data, code, msg).__dict__



if __name__ == '__main__':
    JsonResponse.success(data={'name': '杰克逊'})
