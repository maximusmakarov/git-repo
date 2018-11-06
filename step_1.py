#Транспонирование матрицы
matrix = [[0.5, 0, 0, 0, 0],
         [1, 0.5, 0, 0, 0],
         [1, 1, 0.5, 0, 0],
         [1, 1, 1, 0.5, 0],
         [1, 1, 1, 1, 0.5]]

# Транспонирование
matrix_t = list(zip(*matrix))

# Вывод матриц
# print(matrix)
# print(matrix_t)

for row in matrix:
   print(row)
   # print(sum(row))

print('*' * 25)
for row in matrix_t:
   print(row)


a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [100, 200, 300, 400, 500, 600]

# [(1, 10, 100), (2, 20, 200), ...]

# result = zip(a, b, c)
# print(list(result))

args = [a, b, c]

result = zip(*args)
print(list(result))

# dict
