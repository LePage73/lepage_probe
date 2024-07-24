# Функции в Python.Функция с параметром

def get_matrix (n , m, value):
    matrix =[]
    for i in list(range(n)):
        matrix.append([])
        for j in list(range(m)):
            matrix[i].append(value)
    return matrix

result = get_matrix(2,2,10)
result2 = get_matrix(3,5,42)
result3 = get_matrix(4,2,13)


print(result)
print(result2)
print(result3)