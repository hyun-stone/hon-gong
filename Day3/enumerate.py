# 변수 선언
example_list = ["요소A", "요소B", "요소C"]

# 그냥 출력
print("# 단순 출력")
print(example_list)
print()

# enumerate() 함수 적용
print("# enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

# list() 함수로 강제 변환 후 출력
print("#list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

# for 반복문과 enumerate() 함수 조합
print("# 반복문과 조합")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))