from random import randint
from flask import request
# code=[]
# for i in range(6):
#     code.append(str(randint(0, 9)))
code=[str(randint(0,9)) for i in range(6)]
code = ''.join(code)
print(code)