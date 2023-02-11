def task5():
    students = list()
    students = []
    sections = []

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
                print()
task5()