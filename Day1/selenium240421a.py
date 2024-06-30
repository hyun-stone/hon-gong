import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 크롬 드라이버 생성
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Google 웹사이트 접속
driver.get("https://www.google.com")

# 검색 입력창 찾기 (검색창 이름 'q')
search_box = driver.find_element(By.NAME, 'q')

# 검색어 입력
search_box.send_keys('Jennie')

# 검색 실행
search_box.submit()
time.sleep(5)

# 결과 페이지 스크린샷 저장
driver.save_screenshot('search_results.png')

# 브라우저 종료
driver.quit()

 