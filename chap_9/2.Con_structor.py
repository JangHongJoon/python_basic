class Student:
    def __init__(self, name,korean):
        self.name = name
        self.korean = korean


students=[
    Student("장홍준",56),
    Student("김민수",45),
    Student("정수민",50)
]

print(students[0].name)
print(students[1].korean)