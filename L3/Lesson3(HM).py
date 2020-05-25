# def divide(a, b):
#     res = a / b
#     print(res)
# try:
#     divide(1, 0)
# except ZeroDivisionError as e:
#     print(e.args)
#==============================
def name_input(a):
    new_name = open('../words.txt', 'w', encoding='utf-8')
    new_name.write(str(a) + '\n')

name_input(input('print your name:'))

def read():
    con = open('../words.txt', 'r', encoding='utf-8')  # open new file
    all_lines = con.readlines()  # read all lines from file
    for line in all_lines:
        print(line, end='')
    con.close()

read()


