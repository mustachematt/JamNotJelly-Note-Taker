#create a new account, assert My Notes in title
#after completion
#precondition: no account
#postcondition: created account, successfully in My Notes

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/Google/Chrome/chromedriver.exe')

driver.get("http:localhost:5000")
assert "Jelly Lists" in driver.title

usernameField = driver.find_element_by_id("username")
ActionChains(driver).move_to_element(usernameField).click().perform()
usernameField.send_keys("TestAccount3")

emailField = driver.find_element_by_name("email")
ActionChains(driver).move_to_element(emailField).click().perform()
emailField.send_keys("arealemail3@kent.edu")

passwordField = driver.find_element_by_name("password")
ActionChains(driver).move_to_element(passwordField).click().perform()
passwordField.send_keys("StealthyPassword")

password2Field = driver.find_element_by_name("password2")
ActionChains(driver).move_to_element(password2Field).click().perform()
password2Field.send_keys("StealthyPassword")
password2Field.send_keys(Keys.RETURN)

if("My Notes" in driver.title):
    print("found my notes in title, success!")

sleep(2)
driver.close()