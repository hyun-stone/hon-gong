# 리스트 선언 후 뒤집기
list_a = [1, 2, 3, 4, 5]
list_reversed = reversed(list_a)

# 출력
print("# reversed() 함수")
print("reversed([1, 2, 3, 4, 5]) :", list_reversed)
print("list(reversed([1, 2, 3, 4, 5])) :", list(list_reversed))
print()

# 반복문 적용
print("# reversed() 함수와 반복문")
print("for i in reversed([1, 2, 3, 4, 5]) :")
for i in reversed(list_a):
    print("-", i)