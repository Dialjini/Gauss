x_list = ['1', '2', '3']

def erase(main_col, erase_col, pos):
    multiplier = main_col[pos]
    for i in range(pos, len(erase_col)):
        if main_col[pos] <= 0:
            main_col[i] = main_col[i] + erase_col[i] * multiplier
        elif main_col[pos] > 0:
            main_col[i] = main_col[i] - erase_col[i] * multiplier
    return main_col

def small_replace(list, public_pos, protected_pos):
    glass = list[public_pos]
    list[public_pos] = list[protected_pos]
    list[protected_pos] = glass

    glass = x_list[public_pos]
    x_list[public_pos] = x_list[protected_pos]
    x_list[protected_pos] = glass

    return

def refresh_pos(matrix, pos):
    max_pos = pos
    max_value = matrix[pos][pos]
    for i in range(len(matrix[pos]) - 1):
        if max_value < matrix[pos][i]:
            max_value = matrix[pos][i]
            max_pos = i

    if max_pos == pos:
        return

    for i in matrix:
        small_replace(list=i, public_pos=pos, protected_pos=max_pos)
    return



def divide(matrix, pos):
    divider = matrix[pos][pos]
    for i in range(pos, len(matrix[pos])):
        matrix[pos][i] /= divider
    return

def get_answer(matrix):
    result = ['x{0} = '.format(x_list[0]), 'x{0} = '.format(x_list[1]), 'x{0} = '.format(x_list[2])]

    a = matrix[2][3] / matrix[2][2]
    result[0] += str(a)
    b = (matrix[1][3] - a * matrix[1][2]) / matrix[1][1]
    result[1] += str(b)
    c = (matrix[0][3] - a * matrix[0][2] - b * matrix[0][1]) / matrix[0][0]
    result[2] += str(c)

    string = ''
    for i in result:
        string += i
        string += ', '

    string = string[:-2]
    return string


def solve(matrix):
    cols = len(matrix)
    refresh_pos(matrix=matrix, pos=0)
    divide(matrix=matrix, pos=0)
    matrix[cols - 1] = erase(main_col=matrix[cols - 1], erase_col=matrix[0], pos=0)
    matrix[cols - 2] = erase(main_col=matrix[cols - 2], erase_col=matrix[0], pos=0)
    refresh_pos(matrix=matrix, pos=1)
    divide(matrix=matrix, pos=1)
    matrix[cols - 1] = erase(main_col=matrix[cols - 1], erase_col=matrix[1], pos=1)

    return get_answer(matrix=matrix)
