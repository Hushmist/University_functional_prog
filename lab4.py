def task1():
    #1
    str1 = "lower"
    print(str1.islower())
    #2
    print(chr(120))
    #3
    str3 = "   spaces"
    print(str3.lstrip())
    #4
    str4 = "a some text needs title case"
    print(str4.title())
    #5
    str5 = "long long text"
    print(str5.count("long"))
    #6
    str6 = "561"
    print(str6.isdigit())
    #7
    str7 = "2"
    print(ord(str7))
    #8
    str8 = "needs replace j"
    print(str8.replace('j', 'h'))
    #9
    str9 = "needs find that letter"
    print(str9.find('let'))
    #10
    str10 = "needs split that string"
    print(str10.split())

def task2():
    students = {}
    students['alfa'] = 15
    students['beta'] = 2
    print(sorted(students))

task2()
