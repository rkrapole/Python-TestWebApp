'''
Created on Jan 12, 2021

@author: rkrap
'''
from selenium import webdriver
import time
from selenium.webdriver.firefox import webelement

driver = webdriver.Chrome(executable_path="C:\\DevSecOps\chromedriver.exe")
driver.maximize_window()

driver.get("http://localhost:6060/RkmavenProject_Test/")
time.sleep(2)

buttontext = driver.find_element_by_xpath(".//*[@value='SEND MESSAGE']").get_attribute('value')

print(buttontext)
if buttontext == 'SEND MESSAGE':
    print("Verification Passed")
else :
    print("Verification Failed")

driver.refresh()

driver.close()