# import datetime
# print (datetime.datetime.now())
# #===============================
# import requests
# import time
# for i in range(5):
#     r = requests.get('https://github.com')
#     if r.status_code != 200:
#         print('something is not ok')
#     else:
#         print('everything is ok')
#     time.sleep(5)

# =================================
# import requests
# import time
#
# url_to_test = input('url:')
# for i in range(5):
#     r = requests.get(str(url_to_test))
#     if r.status_code != 200:
#         print('something is not ok')
#     else:
#         print('everything is ok')
#     time.sleep(5)

# ======================--file---===================
# contents = open('read_my_content.txt', 'r')  # open new file
# all_lines = contents.readlines()  # read all lines from file
# for line in all_lines:
#     print(line, end='')
# contents.close()
# # ------------------write to file--------------------
# input_from_user = input('enter line to save in file:')  #
# line_desc = open('read_my_content.txt', 'a')
# line_desc.write(str(input_from_user) + '\n')  # write in the next line

# ========================================


def new_name_input(a):
    new_name = open('../names.txt', 'a')
    new_name.write(str(a) + '\n')


new_name_input(input('print a new name:'))
new_name_input(input('print a new name:'))
new_name_input(input('print a new name:'))


def read_file():
    contents = open('../names.txt', 'r')  # open new file
    all_lines = contents.readlines()  # read all lines from file
    for line in all_lines:
        print('bless you', line, end='')
    contents.close()



read_file()


# ----------------------------Errors(try,except)-----------------------

#if you want devide 0
a = int(input("enter 1st num:"))
b = int(input("enter 2nd num:"))
try:
    res = a / b
except ZeroDivisionError as e:                    #
    print('error is ' + str(e.args))              #
    res = -1

print('the res is:' + str(res))