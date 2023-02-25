import random

def example():
    my_list = [5, 7]
    my_list.append(1)
    my_list.count(5)
    my_list.pop()
    my_list.sort()
    my_list.insert(1, 77)
    print(my_list)

def task1():
    students = list()
    students = []

    students.append(['Alfa', "Section1"])
    students.append(['Beta', "Section2"])
    students.append(['Gamma', "Section1"])
    students.append(['Delta', "Section3"])
    
    while(len(students) > 0):
        selected = students[0][1]
        for i in range(len(students)):
            try:
                if(students[i][1] == selected):
                    print(students.pop(i))
            except:
                print(end='')

def task2():
    students = []
    students.append(['Alfa', 5])
    students.append(['Beta', 3])
    students.append(['Gamma', 4])
    students.append(['Delta', 5])

    choosen = input('Enter student name')
    for i in students:
        if(i[0] == choosen):
            print(i[1])

def task3_4(is_desc = False):
    numbers = []
    inputed = 1
    
    while(1):
        inputed = int(input("enter number(0 - stop)"))
        if(inputed == 0):
            break
        numbers.append(inputed)
    if(is_desc):
        numbers.sort(reverse=True)
    else:
        numbers.sort()
    for i in numbers:
        print(i)

def task5():
    numbers = []
    for i in range(1, 50):
        numbers.append(i)
    res = []
    for i in range(6):
        res.append(numbers.pop((random.randint(a=0,b=len(numbers)))))
    return res

def is_sorted(numbers):
    return numbers == sorted(numbers)

# example()
task1()
# task2()
# task3_4()
# task3_4(True)
# print(task5())
# print(is_sorted([1, 2]))