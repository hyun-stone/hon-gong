# 모듈 가져오기
import math

# 클래스 선언
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference (self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    # 게터와 세터 선언
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

# 원의 둘레와 넓이
circle = Circle(10)
print("# 원의 둘레와 넓이 구하기")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())
print()

# 간접적으로 __radius에 접근
print("# __radius에 접근합니다.")
print(circle.get_radius())
print()

# 원의 둘레와 넓이
circle.set_radius(2)
print("# 반지름을 변경하고 원의 둘레와 넓이 구하기")
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())