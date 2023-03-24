import functools # для Reduce

# task 2

def getArr():
    return ['some', 'random', 'data']


def getTuple():
    return ('this', 'is', 'a', 'tuple')


def getDict():
    return {'get': 'data'}

# task 3


def getMap():
    some_list = [5, 4, 6]
    return list(map(lambda x: x * 2, some_list))


def getFilteterdList_(someList):
    return list(filter(lambda x: True if x > 0 else False, someList))


def getReducedData(someList):
    return (functools.reduce(lambda x, y: x if x > y else y, someList)) #reduse - сократить

def getReducedData_(someList):
    return (functools.reduce(lambda x, y: x + y, someList))

someList = [-9, 2, 3]

# print(getFilteterdList_(someList))
# print(getReducedData(someList))
# print(getReducedData_(someList))

## task 4



def deliveryPrice(street, price):
    streetsInSquare = ['Al-phrabi', 'Saina', 'Tashekent', 'Dostyk', 'Shefchenko']
    streetsOffSquare = ['Monke bi', 'Momysh-uly']
    if(street in streetsOffSquare):
        return 1000
    if(street in streetsInSquare):
        if(price > 10000):
            return 0
        return 500
    return 'Wrong street'
    # return 1000 if street in streetsOffSquare else 0 if street in streetsInSquare else 500

# print(deliveryPrice('Monke bi', 23000))

def kompositionFunctions(f, g):
    return lambda someString: f(g(someString)) 

def f(someString):
    return someString.upper()

def g(someString):
    return someString.lower()
        
shit = kompositionFunctions(f, g)('x')
print(shit)
# print(shit('Help'))



