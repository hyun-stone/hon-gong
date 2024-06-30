# 변수를 선언합니다.
score = float(input("학점 입력 >"))

# 조건문을 적용합니다.
if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자")
else:
    print("일반인")
    