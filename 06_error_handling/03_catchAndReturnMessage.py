def catchAndReturnMessage(message: str, main_function: callable) -> str:
    try:
        # invoke the callable
        main_function()

        # return message if exception is not raised
        print(message)
        return message
    except Exception as err:
        print(err)
        raise


# def add_zeros():
#     return 0
#
#
# function_var = add_zeros
#
# catchAndReturnMessage(message='this is callable', main_function=function_var)
