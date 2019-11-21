#jnj website webdriver

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
driver = webdriver.Chrome(executable_path=r'/home/travis/virtualenv/python3.6.7/bin/chromedriver.exe')

# For testing on PA
driver.get("https://mustachematt.pythonanywhere.com")
# For testing on local server
#driver.get("http:localhost:5000")
assert "Jelly Lists" in driver.title

#signUpButton = driver.find_element_by_id("signUpButton")
#ActionChains(driver).move_to_element(signUpButton).click().perform()


loginButton = driver.find_element_by_id("loginButton")

ActionChains(driver).move_to_element(loginButton).click().perform()

usernameField = driver.find_element_by_id("username")
ActionChains(driver).move_to_element(usernameField).click().perform()

usernameField.send_keys("shannon")

passwordField = driver.find_element_by_id("password")
ActionChains(driver).move_to_element(passwordField).click().perform()

passwordField.send_keys("420")
passwordField.send_keys(Keys.RETURN)

assert "My Notes" in driver.title

print("Login webdriver test passed! :-]")

sleep(2)
driver.close()
