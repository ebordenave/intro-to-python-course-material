
def catchCleanupAndThrow(main_supplier:callable, index_supplier:callable, zero_supplier:callable, cleanup:callable) -> str:
    try:
        # invoke the callable
        main_function()

        # return message if exception is not raised
        print(message)
        return message
    except Exception as err:
        print(err)
        raise