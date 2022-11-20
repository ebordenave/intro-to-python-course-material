def catchAndReturnMessage(message: str, main_function: callable) -> str:
    try:
        # invoke the callable
        main_function()

        # return message if exception is not raised
        # print(message)
        return message
    except Exception as err:
        print(err)
        raise


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
