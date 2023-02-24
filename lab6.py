import random

def tuple_examples():
    my_tuple = ("Besken", "Nurtai", 19, "Anime")

    print(my_tuple)

def set_examples():
    my_set = {"Besken", "Nurtai", 19, "Anime"}
    print(my_set)

def task1():
    first_tuple = ("123", "123")
    print(first_tuple)

def task1fill(user_tuple, a, b):
    user_tuple = ('123', '123')
    for i in range(10):
        user_tuple.__add__('123')
    print(user_tuple)

# tuple_examples()
# set_examples()
task1()