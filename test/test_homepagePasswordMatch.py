#chromedriver script that tests for password matching
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

usernameField = driver.find_element_by_id("username")
ActionChains(driver).move_to_element(usernameField).click().perform()
usernameField.send_keys("shaqueequee")

emailField = driver.find_element_by_name("email")
ActionChains(driver).move_to_element(emailField).click().perform()
emailField.send_keys("smorri55@kent.edu")

passwordField = driver.find_element_by_name("password")
ActionChains(driver).move_to_element(passwordField).click().perform()
passwordField.send_keys("420")

password2Field = driver.find_element_by_name("password2")
ActionChains(driver).move_to_element(password2Field).click().perform()
password2Field.send_keys("419")
password2Field.send_keys(Keys.RETURN)

passConfirmError = driver.find_element_by_name("confirmPass")
string1 = passConfirmError.get_attribute('innerHTML')
print(string1)

if(string1.find("Field must be equal to password.")) == -1:
    print("test failed.")
else:
    print("TEST PASSED!")
sleep(2)





driver.close()