#https://github.com/Hushmist/University_functional_prog
from random import randint, random, randrange

#1 2
def task_1_2():

    arr = ['blue', 'black']
    for i in arr:
        print(i)
    some_bool = True
    while (some_bool):
        some_bool = False
        
    for i in range(1, 5):
        print(i)

#3
def task_3():
    print(randint(0, 10))
    print(randrange(5))
    print(random())
    for i in enumerate(arr):
        print(i)

#4
def my_range(a, b):
    if a < b: 
        for i in range(a, b+1):
            print(i)
    else:
        for i in range(a, b-1, -1):
            print(i)

def odd_dsec(a, b):
    #a > b
    for i in range(a, b-1, -1):
        if(i%2 != 0):
            print(i)
#В галлерий
def cards(n):
    list = []
    for i in range(1, n):
        data = int(input("Input number ")) 
        list.append(data)
    for i in range(1, n+1):
        is_isset = False
        for j in list:
            if(j == i):
                is_isset = True
        if(is_isset == False):
            print(i)


a = 5
b = 10
# my_range(a, b+1)
# my_range(b, a)
# odd_dsec(b, a)
the_n = int(input("Enter N "))
cards(the_n)
