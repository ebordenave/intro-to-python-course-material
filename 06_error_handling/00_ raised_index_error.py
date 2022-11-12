
def raiseIndexError(v):
    ls = [1, 2, 3]
    if v > len(ls):
        raise IndexError('index error')
    return None


raiseIndexError(5)
