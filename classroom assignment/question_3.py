check = True
while check:
    try:
        Student = []
        sid, name, gender, course, cgpa = input(
            'enter sid,name,gender,course,cgpa : ').split()
        Student.append(int(sid))
        Student.append(name)
        Student.append(gender)
        Student.append(course)
        Student.append(float(cgpa))
    except:
        print("enter data in correct form and enter all ")
    else:
        print(Student)
        check = False
