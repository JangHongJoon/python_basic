class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def __init__(self):
        Person.__init__(5)

james = Student()
james.greeting()