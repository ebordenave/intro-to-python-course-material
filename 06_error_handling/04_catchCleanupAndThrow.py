def catchCleanupAndThrow(main_supplier: callable, index_supplier: callable, zero_supplier: callable,
                         cleanup: callable) -> str:
    # try main_supplier
    try:
        return main_supplier()
    except IndexError:
        return index_supplier()
    except ZeroDivisionError:
        return zero_supplier()
    finally:
        cleanup()
