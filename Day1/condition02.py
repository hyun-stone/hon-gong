# 입력을 받습니다.
number = input("정수 입력 >")
last_character = number[-1]

# 짝수 조건
if last_character in "02468":
    print("{}로 끝나는 수는 짝수입니다.".format(last_character))

# 홀수 조건
if last_character in "13579":
    print("{}로 끝나는 수는 홀수입니다.".format(last_character))
