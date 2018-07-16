class Student:
    count = 0
    def __init__(self,name,korean,math):
        self.name=name
        self.korean=korean
        self.math=math

        Student.count +=1
        print("{}번쨰 학생이 생성되었습니다.".format(Student.count))

students =[
    Student("장홍준",87,99),
    Student("박은표",88,99)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))