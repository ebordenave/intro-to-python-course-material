try:
    raise RuntimeError("this is my message")
except Exception as e:
    print(f"the message of the exception => {e}")


# this is one of the hw assignments