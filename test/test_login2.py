#chromedriver script that tests for password matching
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/Google/Chrome/chromedriver.exe')

#driver.get("https://mustachematt.pythonanywhere.com")
driver.get("http:localhost:5000")
assert "Jelly Lists" in driver.title

loginButton = driver.find_element_by_id("loginButton")
ActionChains(driver).move_to_element(loginButton).click().perform()

usernameField = driver.find_element_by_id("username")
ActionChains(driver).move_to_element(usernameField).click().perform()
usernameField.send_keys("shaqueeee")

passwordField = driver.find_element_by_name("password")
ActionChains(driver).move_to_element(passwordField).click().perform()
passwordField.send_keys("420")
passwordField.send_keys(Keys.RETURN)

invalidnameorpassError = driver.find_element_by_name("invalidnameorpassError")
string1 = invalidnameorpassError.get_attribute('innerHTML')
print(string1)

if(string1.find("Invalid username or password")) == -1:
    print("test failed.")
else:
    print("TEST PASSED!")
sleep(5)

#sleep(10)
#sleep(30)
#print(emailError)
#ActionChains(driver).move_to_element(loginButton).click().perform()
#usernameField = driver.find_element_by_id("username")
#ActionChains(driver).move_to_element(usernameField).click().perform()
#if(string1.find("Invalid email address.")) == -1:
    #print("test failed.")
#usernameField.send_keys("shannon")



#passwordField = driver.find_element_by_id("password")
#ActionChains(driver).move_to_element(passwordField).click().perform()
#passwordField.send_keys("420")
#passwordField.send_keys(Keys.RETURN)

#assert "My Notes" in driver.title

#print("Login webdriver test passed! :-]")

#sleep(2)
driver.close()