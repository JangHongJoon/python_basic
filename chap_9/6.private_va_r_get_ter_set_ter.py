import math
class Circle:
    def __init__(self,radius):
        self.__radius = radius  # __ 를 붙히면 외부에서 사용을 못 함

    def get_circumference(self):
        return 2 * math.pi * self.__radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)

print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

print(circle.__radius) # __ 를 붙히면 외부에서 사용을 못 함