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
    name = True
    while(True):
        name = input("Enter last name: ")
        if(name == ''):
            break
        student_class = int(input("Enter class: "))
        students[name] = student_class
    print(sorted(students.items(), key=lambda students: students[1]))

def task2_alternative():
    students = []
    courses = []

    students.append('Alfa')
    courses.append(5)
    students.append('Beta')
    courses.append(2)
    students.append('Gamma')
    courses.append(3)

    for i in range(0, len(students) - 1):
        min = courses[i]
        selected = i
        for j in range(i, len(students)):
            if(courses[j] < min):
                min = courses[j]
                selected = j
        temp = courses[i]
        courses[i] = courses[selected]
        courses[selected] = temp

        temp_s = students[i]
        students[i] = students[selected]
        students[selected] = temp_s

    print(courses)
    print(students)

def task3(str = ""):
    upper_count = 0
    lower_count = 0
    for i in str:
        if(i.islower()):
            lower_count = lower_count+1
        else:
            upper_count = upper_count+1 
    return str.upper() if upper_count > lower_count else str.lower() # тринарный оператор 

def tast3_2():
    while(1):
        num1 = input("Enter first number ")
        num2 = input("Enter second number ")
        if(num1.isdigit() and num2.isdigit()):
            break
        print("Error: 404")
    return (int(num1) + int(num2))

task2_alternative()