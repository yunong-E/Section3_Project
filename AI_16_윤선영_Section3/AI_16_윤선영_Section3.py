# -*- coding: utf-8 -*-
import requests
import selenium
import time
import re

from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium import webdriver

import pymysql.cursors
import mysql.connector




### ------- Connect to the database (mySQL) ------- ###
conn = mysql.connector.connect(
    host="localhost",
    database="AI_16_윤선영_Section3",
    user="hello",
    password='1111')

cursor = conn.cursor(prepared=True)




### ------------- Normal Numbers ------------- ###
def getNumber():
    raw_id = soup.find_all('strong')[9].text
    id = int(re.sub(r'[^0-9]', '', raw_id)) # 회차 정보 크롤링

    num_list = []

    num_list.append(int(soup.find('span', class_='num large').text))  # 첫째 번호
    for i in range(1, 7):
        num_list.append(int(soup.find('span', class_=f"num al720_color{i}").text)) # 나머지 6개 번호

    cursor.execute("INSERT INTO Raw_Lottery VALUES(?, ?, ?, ?, ?, ?, ?, ?);", 
            (id, num_list[0], num_list[1], num_list[2], num_list[3], num_list[4], num_list[5], num_list[6])) # DB 저장

    conn.commit()

    return




### ------------- Bonus Numbers ------------- ###
def getBonus():
    test = []
    bonus_list = []

    raw_id = soup.find_all('strong')[9].text
    id = int(re.sub(r'[^0-9]', '', raw_id)) # 회차 정보 크롤링

    for i in range(6):
        test.append(soup.select('td.ta_right > div.win720_num > span.num'))

    test = test[-1]

    for i in range(27, 33):
        bonus_list.append(int(test[i].text))
    
    cursor.execute("INSERT INTO Raw_Bonus VALUES(?, ?, ?, ?, ?, ?, ?);", 
        (id, bonus_list[0], bonus_list[1], bonus_list[2], bonus_list[3], bonus_list[4], bonus_list[5])) # DB 저장

    conn.commit()

    return




### 동행복권의 경우 동적 크롤링이 필요.
service = Service('/Users/yun/Downloads/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://dhlottery.co.kr/gameResult.do?method=win720')

idx = 139
test_list = []

while True:
    
    select_dir = Select(driver.find_element(By.ID, "Round")) # 콤보박스에 해당하는 ID check
    try:
        time.sleep(1)
        select_dir.select_by_value(str(idx))
        time.sleep(0.5)
        driver.find_element(By.ID, "searchBtn").send_keys(Keys.ENTER)
        time.sleep(0.5)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        getNumber() # 1등정보 가져오기
        getBonus() # 보너스 번호 가져오기

    except selenium.common.exceptions.NoSuchElementException:
        print('예외처리')
        break

    idx-=1

    # 회차가 0이 되면 종료
    if idx == 0:
      break   




### ------------- Test ------------- ###
# url = 'https://dhlottery.co.kr/gameResult.do?method=win720'
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

# ### 응답상태 확인
# try:
#     resp = requests.get(url)
#     resp.raise_for_status()

# except HTTPError as Err:
#     print('HTTP 에러가 발생했습니다.')

# except Exception as Err:
#     print('다른 에러가 발생했습니다.')

# else:
#     print('성공')
### ------------------------------------- ###




### ------- Save in database (Bonus Numbers) ------- ###
# for i in range(6):
#     cursor.execute("INSERT INTO Lottery VALUES(?, ?, ?, ?, ?, ?, ?, ?)", bonus_list[i]) # 성공

# conn.commit()
# cursor.execute("SELECT * FROM Lottery")