# 1 task
def task1():
    list1 = [88, 12, 15, 20, 25]
    list2 = [2, 4, 6, 8, 10]

    if all(x > max(list2) for x in list1):
        pairs = list(zip(list1, reversed(list2)))
        print(list(enumerate(pairs)))
        averages = []
        for i, pair in enumerate(pairs):
            average = sum(pair) / 2
            averages.append(round(average, 2))
        print("Average", averages)
    else:
        print("Не все элементы первого массива больше чем второй массив")
task1()
# print(example1([10, 5]))

# 2.1 task
#  Напишите программу, которая считывает строку с клавиатуры и 
# выводит на экран все уникальные символы в этой строке в алфавитном 
# порядке. Для этого необходимо использовать встроенные функциию
def unique_strings(some_string):
    some_string = set(some_string)
    return sorted(some_string)
# 2.2  Напишите программу на Python, которая использует встроенную 
# функцию any() для проверки, есть ли в списке хотя бы один элемент, 
# удовлетворяющий заданному условию. Затем используйте встроенную 
# функцию all() для проверки, удовлетворяют ли все элементы списка 
# заданному условию 
def _any(some_string):
    new_string = 'qwerty'
    return any(some_string in x for x in new_string)
def _all(some_string):
    new_string = 'qqqqq'
    return all(some_string in x for x in new_string)
    
# print(unique_strings('aaabaaavf'))
# print(_any('b'))
# print(_all('q'))

# 2.3 Реализуйте функцию, которая принимает матрицу (список списков) и 
# возвращает матрицу, повернутую на 90 градусов по часовой стрелке. 
# Используйте функции zip(), list() и reversed()(
def _rotate(matrix):
    _reversed = reversed(matrix)
    zipped = list(zip(_reversed))
    return zipped

# print(_rotate([[2,5],
#                [7,9]]))

def knapsack(weights, costs, max_weight):
    n = len(weights)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + costs[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][max_weight]

# weights = [10, 20, 30]
# costs = [60, 100, 120]
# max_weight = 50
# print(knapsack(weights, costs, max_weight))

def matrix_operation(matrix1, matrix2, operation):
    if operation == '+':
        return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    elif operation == '-':
        return [[matrix1[i][j] - matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    elif operation == '*':
        return [[sum([matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))]) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    else:
        return None
    
# matrix1 = [[1, 2], [3, 4]]
# matrix2 = [[5, 6], [7, 8]]
# operation = '+'
# print(matrix_operation(matrix1, matrix2, operation))