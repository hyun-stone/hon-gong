# 딕셔너리 선언
dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임"
}

# 내용 출력
print("요소 제거 이전 :", dictionary)

# 딕셔너리 요소 제거
del dictionary["name"]
del dictionary["type"]

# 요소 제거 후에 내용을 출력해 봅니다.
print("요소 제거 이후 :", dictionary)