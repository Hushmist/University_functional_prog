import random
def tuple_examples():
    my_tuple = ("Besken", "Nurtai", 19, "Anime")

    print(my_tuple)

def set_examples():
    my_set = {"Besken", "Nurtai", 19, "Anime"}
    print(my_set)

def task1():
    first_tuple = task1fill(0, 5)
    second_tuple = task1fill(-5, 0)
    sum_tuple = first_tuple + second_tuple
    return int(sum_tuple.count(0))

def task1fill(a, b):
    user_tuple = tuple()
    for i in range(10):
        user_tuple = user_tuple + (random.randint(a, b),)
    return user_tuple

def taks2():
    my_tuple = (1,(2.2, ("str",tuple())))
    return (my_tuple[1][1][0])

def task3():
    my_tuple = tuple()
    for i in ['транспортные расходы', 'обед', 'retouran', 'computer club']:
        cost = int(input('Enter cost of ' + i))
        my_tuple = my_tuple + (i, cost)
    sum = 0
    for i in [1,3,5,7]:
        sum = sum + (my_tuple[(i)])
    return sum

def task4():
    students_str = input()
    students = students_str.split(' ')
    for i in students:
        if(i.find('ва')> -1):
            print(i)

def task5():
    kk_str = input("Enter kk string")
    trans = {
        'а':'a',
        'б':'b',
        'в':'v',
        'г':'g',
        'д':'d',
        'ж':'gh',
        'ч':'ch'
    }
    en_str = ''
    for i in kk_str:
        en_str = en_str + (trans[i])
    return en_str
# tuple_examples()
# set_examples()
# print(task1())
# print(taks2())
# print(task3())
# (task4())
print(task5())
