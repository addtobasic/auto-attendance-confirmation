from selenium import webdriver
import time
import random
from key import EMAIL, PASSWORD, CLASS_URL
# from trueKey import EMAIL, PASSWORD, CLASS_URL

driver = webdriver.Chrome("./chromedriver")
driver.get(CLASS_URL)

login_id_xpath = '//*[@id="identifierNext"]'
login_pw_xpath = '//*[@id="passwordNext"]'

driver.find_element_by_name("identifier").send_keys(EMAIL)
time.sleep(2)
driver.find_element_by_xpath(login_id_xpath).click()

#ネットが遅いのでsleep
time.sleep(5)

driver.find_element_by_name("password").send_keys(PASSWORD)
time.sleep(2)
driver.find_element_by_xpath(login_pw_xpath).click()
