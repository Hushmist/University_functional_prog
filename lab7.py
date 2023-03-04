def examples():
    my_dictionary = {
        'name': 'Nurtai',
        'age': 19,
    }
    #
    print(len(my_dictionary))

    #
    print(my_dictionary.values())

    #
    my_dictionary.popitem()
    print((my_dictionary))

    #4
    my_dictionary.update({'name':'Hushmist'})
    print((my_dictionary))

    #5
    my_dictionary.clear()
    print((my_dictionary))


def task1():
    n = 2
    dict = {
        'esil': 'Kaz',
        'amazomka': 'Brazil',
    }
    reviers = ['esil', 'nil', 'amazomka']

    for i in reviers:
        print(i)

    for i in reviers:
        if(i in dict):
            print(dict[i])
        else:
            print(f'{i} not fount')
        
    for i in reviers:
        print(i in dict)

    dict['Lena'] = 'Rus'
    print(dict)

def task2():
    comments = {
        'Alfa': 'good',
        'Beta': 'good',
        'Delta': 'nice',
        'Gamma': 'awesome'
    }
    values = comments.values()
    unique_val = set(values)
    return len(unique_val)

def task3():
    n = 2
    dict = {
        'Alfa': '+7 707 888',
        'Beta': '+7 707 889'
    }
    name = input('Enter name: ')

    if(name in dict):
        print(dict[name])
    else:
        print(f'{name} not fount')

def task4():
    n = 2
    dict = {
        'Besken Nurtai': ['March', 25],
        'Vasya Pupkin ': ['June', 15],
        'Galya Vedyashkina': ['June', 15]
    }
    # month = 'June'
    month = input('Enter month: ')
    print(f'employee on vacation in {month}: ', end='')
    for key in dict:
        if(month == dict[key][0]):
            print(key, end=' ')
examples()
# task1()
# print(task2())
# task3()
# task4()