# s = '17'
# print(s.isnumeric())
#
# ls = ['a']
# ls.append(s)
# print(ls)
#
#
# def check(inp):
#     try:
#         inp = inp.replace(',', '.')
#         num_float = float(inp)
#         num_int = int(num_float)
#         return num_int == num_float
#     except ValueError:
#         return False
#
#
# print([check(s) for s in ls])

################################
ls = []

my_var = 'a'
ls.append(my_var)
print(ls)

for i in ls:
    my_bool = (isinstance(i, int))
    print(my_bool)
    try:
        if my_bool is True:
            print("its true")
    except ValueError:
        print('dont work homie')


