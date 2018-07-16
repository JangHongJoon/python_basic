def create_student(name,korean,math,english,science):
    return {
        "name":name,
        "korean":korean,
        "math":math,
        "english":english,
        "science":science
    }

def student_get_sum(student):
    return student["korean"]+student["math"]+\
        student["english"]+student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t\t{}\t\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student))

students = [
    create_student("윤인성",87,98,88,95),
    create_student("장홍준", 27, 38, 81, 92),
    create_student("김수호", 77, 28, 38, 55),
    create_student("김태호", 82, 91, 28, 35),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))
