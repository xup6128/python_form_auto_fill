from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:/Users/user/chromedriver.exe')
url = 'https://docs.google.com/forms/d/e/1FAIpQLSccw9r9mm0x5ZANkVV7GkqoeYq4dQqq6o7Z51qpp11MWO7EOg/viewform'

driver.get(url)

inputs = driver.find_elements(By.CLASS_NAME, 'whsOnd')
inputs[0].send_keys('林于騰')
inputs[1].send_keys(date.today().strftime("%Y/%m/%d"))
inputs[2].send_keys('09')
inputs[3].send_keys('00')
inputs[4].send_keys('36')

checkboxes = driver.find_elements(By.CLASS_NAME, 'AB7Lab')
checkboxes[0].click()
checkboxes[4].click()
checkboxes[8].click()

btnSubmit = driver.find_element(By.CLASS_NAME, 'l4V7wb')
btnSubmit.click()

driver.quit();