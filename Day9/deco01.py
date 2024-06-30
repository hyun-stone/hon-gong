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
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

# 원의 둘레와 넓이
print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원래 원의 반지름:", circle.radius)
circle.radius = 2
print("변경된 원의 반지름:", circle.radius)
print()

# 강제로 예외 발생
print("# 강제로 예외 발생시키기")
circle.radius = -10