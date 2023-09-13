# workout.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# import random
# import time

# rdsec = random.randrange(1,420)

# print("슬립시작:", round(rdsec), "초 간 슬립!!")

# # 랜덤 초간 슬립
# time.sleep(rdsec)

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#chromedriver = './chromedriver.exe'
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get('https://gw.dreamsecurity.com/app/ehr/')

driver.implicitly_wait(1000)

# 아이디 입력
inputid = driver.find_element(By.ID,"username")
inputid.send_keys("horrordream")

# PW 입력
inputpw = driver.find_element(By.ID, "password")
inputpw.send_keys("qkrwlstjr1@@")

# 로그인 버튼 클릭
driver.find_element(By.ID,"login_submit").click()

# 퇴근하기 버튼명 확인
print(driver.find_element(By.ID,"workOut").text)

# 퇴근하기 버튼 클릭
driver.find_element(By.ID,"workOut").click()
