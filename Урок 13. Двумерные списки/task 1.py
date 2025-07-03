import random

x = int(input('Введите количество столбцов: '))
y = int(input('Введите количество строк: ')) 

matrix_1 = [[random.randint(1, 10) for i in range(x)] for j in range(y)]
matrix_2 = [[random.randint(1, 10) for i in range(y)] for j in range(y)]


def sm(c1, c2):
    matrix = [[0 for i in range(x)] for j in range(y)]
    for i in range(len(c1)):
        for j in range(len(c1)):
            matrix[i][j] = c1[i][j] + c2[i][j]
    return matrix

print(matrix_1)
print(matrix_2)
print(matrix_1, matrix_2)







