# 1 task
def task1(max_list, min_list):
    check_list = []
    for x in max_list:
        check_list.append(x > max(min_list))
    if(not all(check_list)):
        return None
    pairs = list(zip(max_list, reversed(min_list)))
    averages = []
    for i, pair in enumerate(pairs):
        average = sum(pair) / 2
        averages.append(round(average, 2))
    return (averages)
print(task1([55, 2, 33], [11, 13, -8]))

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
def _rotate_(matrix):
    _reversed = list(reversed(matrix))
    zipped = (list(zip(_reversed[0], _reversed[1], _reversed[2])))
    return zipped

print(_rotate_([[2,5,5],
               [7,9,6],
               [5,7,3]]))

# 2.4Реализуйте функцию для решения задачи о рюкзаке с помощью 
# динамического программирования. Функция принимает два списка 
# (веса и стоимости предметов) и максимальный вес рюкзака, а 
# возвращает максимальную стоимость, которую можно унести в 
# рюкзаке. Используйте функции range(), enumerate() и max()


# Реализуйте функцию, которая выполняет операции над двумя 
# матрицами (сложение, вычитание, умножение). Функция принимает 
# две матрицы и символ операции, а возвращает результат операции. 
# Используйте функции enumerate(), zip() и len()
def matrix_operation(matrix1, matrix2, operation):
    _list = []
    match operation:
        case '+':
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    _list.append(matrix1[i][j] + matrix2[i][j])
            return _list
        case '-':
            for i in range(len(matrix1)):
                for j in range(len(matrix1[0])):
                    _list.append(matrix1[i][j] - matrix2[i][j])
            return _list
        case '*':
            _new_list = []
            for _, i in enumerate(range(len(matrix1))):
                for j in range(len(matrix2[0])):
                    _list.append([sum([matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))])])
            for i in range(0, len(_list), 2):
                _new_list.append(list(zip(_list[i], _list[i+1])))
            return _new_list
    
print(matrix_operation([[1, 2], [3, 4]], [[5, 6], [7, 8]], '*'))