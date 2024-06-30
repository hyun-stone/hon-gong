# 사용자 정의 예외 생성
class CustomerException(Exception):
    def __init__(self, message, value):
        Exception.__init__(self)
        self.message = message
        self.value = value

    def __str__(self):
        return self.message
    
    def print(self):
        print("##### 오류 정보 #####")
        print("메시지:", self.message)
        print("값:", self.value)

# 예외 발생
try:
    raise CustomerException("딱히 이유 없음", 273)
except CustomerException as e:
    e.print()