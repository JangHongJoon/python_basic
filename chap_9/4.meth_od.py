class Student:
    def __init__(self,name,korean,math):
        self.name = name
        self.korean = korean
        self.math = math

    def get_sum(self):
        return self.korean +self.math

    def get_average(self):
        return self.get_sum() / 2

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())
        
students =[
    Student("장홍준",34,12),
    Student("홍길동", 34, 12),
    Student("김민수", 34, 12)
]
print(students)

print("이름","총점","평균", sep="\t")
for student in students:
    print(student.to_string())