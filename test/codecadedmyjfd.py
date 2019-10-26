from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://codecademy.com")
assert "Codecademy" in driver.title

loginButton = driver.find_element_by_css_selector('[data-testid="header-sign-in"]')

actions = ActionChains(driver)
#actions = move_to_element(loginButton)
actions.click(loginButton)
actions.perform()

ActionChains(driver).move_to_element(loginButton).click(loginButton).perform()




#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
sleep(5)
assert "No results found." not in driver.page_source
driver.close()





