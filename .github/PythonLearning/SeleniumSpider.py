from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.PhantomJS()
browser.get("https://www.bilibili.com/")

input = WAIT.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner_link > div > div > form > input")))
submit = WAIT.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))


input.send_keys('蔡徐坤 篮球')
submit.click()
