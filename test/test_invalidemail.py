#second_webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")


#driver = webdriver.Chrome(executable_path=r'C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://mustachematt.pythonanywhere.com")
driver.get("http:localhost:5000")
assert "Jelly Lists" in driver.title

signUpButton = driver.find_element_by_id("signUpButton")
ActionChains(driver).move_to_element(signUpButton).click().perform()

usernameField = driver.find_element_by_id("username")
ActionChains(driver).move_to_element(usernameField).click().perform()
usernameField.send_keys("shanay")

emailField = driver.find_element_by_name("email")
ActionChains(driver).move_to_element(emailField).click().perform()
emailField.send_keys("asdfjkl")

passwordField = driver.find_element_by_name("password")
ActionChains(driver).move_to_element(passwordField).click().perform()
passwordField.send_keys("420")

password2Field = driver.find_element_by_name("password2")
ActionChains(driver).move_to_element(password2Field).click().perform()
password2Field.send_keys("420")
password2Field.send_keys(Keys.RETURN)

sleep(5)

print("nav to signup successful")



emailError = driver.find_element_by_name("emailError")
string1 = emailError.get_attribute('innerHTML')
print(string1)
#print(emailError)
sleep(5)
#ActionChains(driver).move_to_element(loginButton).click().perform()
#usernameField = driver.find_element_by_id("username")
#ActionChains(driver).move_to_element(usernameField).click().perform()
if(string1.find("Invalid email address.")) == -1:
    print("test failed.")
#usernameField.send_keys("shannon")



#passwordField = driver.find_element_by_id("password")
#ActionChains(driver).move_to_element(passwordField).click().perform()
#passwordField.send_keys("420")
#passwordField.send_keys(Keys.RETURN)

#assert "My Notes" in driver.title

#print("Login webdriver test passed! :-]")

#sleep(2)
driver.close()