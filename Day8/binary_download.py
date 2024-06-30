# 모듈 읽어오기
from urllib import request

# urlopen() 함수로 구글 메인페이지 읽기
target = request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output = target.read()
print(output)

# write binary[바이너리 쓰기] 모드
file = open("output.png", "wb")
file.write(output)
file.close()