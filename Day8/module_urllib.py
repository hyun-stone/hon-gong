# 모듈 읽어오기
from urllib import request

# urlopen() 함수로 구글의 메인 페이지 읽기
target = request.urlopen("https://google.com")
output = target.read()

# 출력
print(output)