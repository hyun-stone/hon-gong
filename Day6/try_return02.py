# 함수 선언
def write_text_file(filename, text):
    # try except 구문 사용
    try:
        # 파일 열기
        file = open(filename, "w")
        # 여러 가지 처리 수행
        return
        #파일에 텍스트 입력
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        # 파일 닫기
        file.close()

# 함수 호출
write_text_file("test.txt", "안녕하세요!")