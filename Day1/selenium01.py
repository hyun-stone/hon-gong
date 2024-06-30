# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Chrome()
#url = 'https://google.com'
#driver.get(url)

#*[@id="input"]

#driver.find_element_by_css_selector('truncate').send_keys('이게정되나')
