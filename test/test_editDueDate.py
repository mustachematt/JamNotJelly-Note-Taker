#chromedriver script that tests for password matching
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# For testing on local server
#driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
# For testing on Travis-CI
driver = webdriver.Chrome(executable_path=r'/home/travis/virtualenv/python3.6.7/bin/chromedriver.exe'

#driver.get("https://mustachematt.pythonanywhere.com")
driver.get("http:localhost:5000")
assert "Jelly Lists" in driver.title

loginButton = driver.find_element_by_id("loginButton")
ActionChains(driver).move_to_element(loginButton).click().perform()

usernameField = driver.find_element_by_id("username")
ActionChains(driver).move_to_element(usernameField).click().perform()
usernameField.send_keys("shannon")

passwordField = driver.find_element_by_name("password")
ActionChains(driver).move_to_element(passwordField).click().perform()
passwordField.send_keys("420")
passwordField.send_keys(Keys.RETURN)

assert "My Notes" in driver.title

pressEdit = driver.find_element_by_name("edit21")
ActionChains(driver).move_to_element(pressEdit).click().perform()

#noteBox = driver.find_element_by_name("note")
#ActionChains(driver).move_to_element(noteBox).click().perform()
#noteBox.clear()
#noteBox.send_keys("new new new note")
dueDate = driver.find_element_by_name("due_date")
ActionChains(driver).move_to_element(dueDate).click().perform()
dueDate.clear()
dueDate.send_keys("12/30/2019")


pressSave = driver.find_element_by_name("submit")
ActionChains(driver).move_to_element(pressSave).click().perform()

if ("12/30/2019" in driver.page_source):
    print("test passed")


sleep(5)




#assert "My Notes" in driver.title

#print("Login webdriver test passed! :-]")

#sleep(2)
driver.close()
