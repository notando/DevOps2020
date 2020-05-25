#===========================DEBUGGING===================
# def add_num(a, b):
#     print('hello')
#     for i in range(10):
#         res = a - b
#         print(res)
# print(1)
# print(2)
# add_num(10, 6)

#===================DECORATORS======================
import datetime
def my_decorator(func):
    def wrapper():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return wrapper()

def bla():
    print("blabla")

@my_decorator
def gaga():
    print('gaga')
try:
    gaga()
except BaseException as e:
    print('Erorr is:'+str(e.args))
