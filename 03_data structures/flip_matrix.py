def flip_matrix(mat: list) -> list:
    result = []
    for i in mat:
        result.insert(0, i)
    # print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in result]))
    return result

