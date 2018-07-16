def create_student(name, korean, math,english,science):
    return{
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

students =[
    create_student("장홍준",45,56,12,67),
    create_student("김심야", 43,26, 11, 27),
    create_student("김로그", 35, 36, 52, 62),
    create_student("마이클장",35, 56, 11, 57),
    create_student("김도연", 45, 26, 32, 47),
    create_student("김민수", 43, 26, 52, 27),
    create_student("장영준", 45, 36, 11, 62),

]

print(students[0]["name"])