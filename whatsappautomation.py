# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("/Users/Mohammad Hanan/chromedriver")
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver,600)
target = '"TA Rishikesh Nanda"'
string = "Message from Python"
x_arg = '//span[contains(@title, '+target+ ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()


input_box = driver.find_element_by_class_name('_1Plpp')
for i in range (50):
    input_box.send_keys(string+Keys.ENTER)