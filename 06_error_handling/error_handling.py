# Catch each error below
# 1)
try:
    int("tree")
except TypeError:
    print("An error occurred")

# 2)
try:
    int("15.99")
except ValueError as err:
    print(f"An error occurred: {err}")
#
# # 3)
# my_list = [1, 2, 3, 4, 5]
# my_list[5]
#
# # 4)
# # *Enter a non-number
# hats = input("How many hats do you own?")
# int(hats)
