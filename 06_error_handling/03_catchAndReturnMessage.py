def catchAndReturnMessage(message: str, main_function: callable) -> str:
    try:
        main_function()
        return message
    except Exception as err:
        return str(err)


# def is_callable(arg) -> bool:
#     var = callable(arg)
#     # print(var)
#     return var
#
#
# def return_zero():
#     return 0
#
#
# # print(is_callable(return_zero))
#
#
# catchAndReturnMessage(message=f'1{print(is_callable(return_zero))}', main_function=return_zero)
