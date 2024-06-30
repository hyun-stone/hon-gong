# try except 구문 사용
try:
    # 파일 열기
    file = open("info.txt", "w")
    # 여러 가지 처리 수행
    예외.발생해라()
except Exception as e:
    print(e)
finally:
    # 파일 닫기
    file.close()

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)