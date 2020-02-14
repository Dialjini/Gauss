from gauss_solver import solve

col = ''
test = []
test_data = True
while col != 'quit':
        col = input('test1 or test2?: ')
        if col == 't1' or col == 'test1':
            test = [[10, -7, 0, 7],
                    [-3, 2, 6, 4],
                    [5, -1, 5, 6]]
            test_data = True
            break
        if col == 't2' or col == 'test2':
            test = [[-3, 1, 2, 5],
                    [4, 2, -1, 0],
                    [2, -3, 1, -1]]
            test_data = True
            break
if not test_data:
    col = int(col)
else:
    col = 3
matrix = []
semi_matrix = []
if not test_data:
    for i in range(col):
        for j in range(col + 1):
            if j != col:
                semi_matrix.append(input('Введите значение коэффициента {0}: '.format(j + 1)))
            else:
                semi_matrix.append(input('Введите результат {0}-го уравнения: '.format(i + 1)))
        matrix.append(semi_matrix)
        semi_matrix = []
else:
    matrix = test

for i in matrix:
    print(i)
print(solve(matrix=matrix))
