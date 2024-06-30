# 함수 선언
def factorial(n):
    # n이 0 이면 1 리턴
    if n == 0:
        return  1
    # n이 0 아니면 n*(n-1)! 리턴
    else:
        return n * factorial(n-1)
    
# 함수 호출
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))