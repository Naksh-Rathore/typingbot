from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard as kb
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://humanbenchmark.com/tests/typing")

time.sleep(1)

text_elements = driver.find_elements(By.CLASS_NAME, "incomplete")

words = [element.text for element in text_elements]

text = ""

for char in words:
    if char == '':
        text += ' '

    else:
        text += char    

kb.wait("ctrl+alt+s")
kb.write(text)

time.sleep(100)
driver.quit()