# try:
#     open('Try[except].py', 'r')
# except ZeroDivisionError as e:
#     print("couldn't divide by zero")
# except FileNotFoundError as e:
#     print('file not found')
# except BaseException as e:
#     print('general error occurred')
# #print('Error is' + str(e.args))

#create my owm error
def get_age():
    age_of_user = int(input("enter your age:")) ##
    if age_of_user < 0:
        raise BaseException('Age cannot be negative error!')   # call red error what will be in base exception

try:
    get_age()
except BaseException as e:
     print('Error is' + str(e.args))
     get_age()
