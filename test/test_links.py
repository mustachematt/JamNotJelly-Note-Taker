#requires requests

import requests
import re
import unittest
from selenium import webdriver


#assign chrome_driver_path to chromedriver.exe below
#chrome_driver_path = ""




driver=webdriver.Chrome(executable_path=r'C:/Program Files (x86)/Google/Chrome/chromedriver.exe')
class test_HomePageLinks(unittest.TestCase):

    def test_0HomePageLinks(self):
        driver.get('https://mustachematt.pythonanywhere.com/')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r=requests.head(link.get_attribute('href'))
            print(r.status_code==200)
            if r.status_code!=200:
                print(r.status_code)
        for link in links:
            if link.text=="Sign Up":
                element=link
        self.assertTrue(element.get_attribute('href')=="https://mustachematt.pythonanywhere.com/register")
        elem=element.get_attribute('href')
        driver.find_element_by_link_text("Sign Up").click()        
        page=driver.page_source
        txt=re.search(r'Confirm Password:',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Login":
                element2=link
        self.assertTrue(element2.get_attribute('href')=="https://mustachematt.pythonanywhere.com/login")
        elem=element2.get_attribute('href')
        driver.find_element_by_link_text("Login").click()
        page=driver.page_source
        txt=re.search(r'Click to Register!',page)
        self.assertNotEqual(txt, None) 
        self.assertTrue(elem==driver.current_url)  

        driver.get('https://mustachematt.pythonanywhere.com/')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/homepage")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("").click()
        page=driver.page_source
        txt=re.search(r'Stay on top',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

    



    def test_1LoginLinks(self):
        driver.get('https://mustachematt.pythonanywhere.com/login')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r=requests.head(link.get_attribute('href'))
            print(r.status_code==200)
            if r.status_code!=200:
                print(r.status_code)
        for link in links:
            if link.text=="Sign Up":
                element=link
        self.assertTrue(element.get_attribute('href')=="https://mustachematt.pythonanywhere.com/register")
        elem=element.get_attribute('href')
        driver.find_element_by_link_text("Sign Up").click()
        self.assertTrue(elem==driver.current_url)
        page=driver.page_source
        txt=re.search(r'Confirm Password:',page)
        self.assertNotEqual(txt, None)
        
        driver.get('https://mustachematt.pythonanywhere.com/login')

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Login":
                element2=link
        self.assertTrue(element2.get_attribute('href')=="https://mustachematt.pythonanywhere.com/login")
        elem=element2.get_attribute('href')
        driver.find_element_by_link_text("Login").click()
        page=driver.page_source
        txt=re.search(r'Click to Register!',page)
        self.assertNotEqual(txt, None) 
        self.assertTrue(elem==driver.current_url)
        driver.get('https://mustachematt.pythonanywhere.com/login')


        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/homepage")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("").click()
        page=driver.page_source
        txt=re.search(r'Stay on top',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)
        
    




    def test_2RegisterLinks(self):
        driver.get('https://mustachematt.pythonanywhere.com/register')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r=requests.head(link.get_attribute('href'))
            print(r.status_code==200)
            if r.status_code!=200:
                print(r.status_code)
        for link in links:
            if link.text=="Sign Up":
                element=link
        self.assertTrue(element.get_attribute('href')=="https://mustachematt.pythonanywhere.com/register")
        elem=element.get_attribute('href')
        driver.find_element_by_link_text("Sign Up").click()
        page=driver.page_source
        txt=re.search(r'Confirm Password:',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)
        driver.get('https://mustachematt.pythonanywhere.com/login')

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Login":
                element2=link
        self.assertTrue(element2.get_attribute('href')=="https://mustachematt.pythonanywhere.com/login")
        elem=element2.get_attribute('href')
        driver.find_element_by_link_text("Login").click()
        page=driver.page_source
        txt=re.search(r'Click to Register!',page)
        self.assertNotEqual(txt, None) 
        self.assertTrue(elem==driver.current_url)
        driver.get('https://mustachematt.pythonanywhere.com/login')


        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/homepage")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("").click()
        page=driver.page_source
        txt=re.search(r'Stay on top',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)







    def test_3Login_MyNotesLinks(self):
        driver.get("https://mustachematt.pythonanywhere.com/login")
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Login":
                element3=link
        username=driver.find_element_by_name("username")
        username.clear()
        username.send_keys("test1")
        password=driver.find_element_by_name("password")
        password.clear()
        password.send_keys("qwerty")
        driver.find_element_by_name("submit").click()

        self.assertTrue(driver.current_url=="https://mustachematt.pythonanywhere.com/mynotes")
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r=requests.head(link.get_attribute('href'))
            print(r.status_code==200)
            if r.status_code!=200:
                print(r.status_code)
                
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/homepage")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("").click()
        page=driver.page_source
        txt=re.search(r'Stay on top',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/mynotes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Account":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/account")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Account").click()
        page=driver.page_source
        txt=re.search(r'Account Page',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/mynotes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Delete Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/delete-notes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Delete Notes").click()
        page=driver.page_source
        txt=re.search(r'Delete All Notes',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/mynotes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="My Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/mynotes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("My Notes").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)


        driver.get('https://mustachematt.pythonanywhere.com/mynotes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Sign Up":
                element=link
        self.assertTrue(element.get_attribute('href')=="https://mustachematt.pythonanywhere.com/register")
        driver.find_element_by_link_text("Sign Up").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(driver.current_url=="https://mustachematt.pythonanywhere.com/mynotes")



    def test_4Account(self):
        driver.get('https://mustachematt.pythonanywhere.com/account')

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r=requests.head(link.get_attribute('href'))
            print(r.status_code==200)
            if r.status_code!=200:
                print(r.status_code)

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/homepage")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("").click()
        page=driver.page_source
        txt=re.search(r'Stay on top',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/account')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="My Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/mynotes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("My Notes").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/account')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Delete Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/delete-notes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Delete Notes").click()
        page=driver.page_source
        txt=re.search(r'Delete All Notes',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/account')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Account":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/account")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Account").click()
        page=driver.page_source
        txt=re.search(r'Account Page',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/account')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Sign Up":
                element=link
        self.assertTrue(element.get_attribute('href')=="https://mustachematt.pythonanywhere.com/register")
        driver.find_element_by_link_text("Sign Up").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(driver.current_url=="https://mustachematt.pythonanywhere.com/mynotes")












    def test_5DeleteNotes(self):
        driver.get('https://mustachematt.pythonanywhere.com/delete-notes')

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r=requests.head(link.get_attribute('href'))
            print(r.status_code==200)
            if r.status_code!=200:
                print(r.status_code)

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/homepage")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("").click()
        page=driver.page_source
        txt=re.search(r'Stay on top',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/delete-notes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="My Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/mynotes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("My Notes").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/delete-notes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Delete Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/delete-notes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Delete Notes").click()
        page=driver.page_source
        txt=re.search(r'Delete All Notes',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/delete-notes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Account":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/account")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Account").click()
        page=driver.page_source
        txt=re.search(r'Account Page',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)
            
        driver.get('https://mustachematt.pythonanywhere.com/delete-notes')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Sign Up":
                element=link
        self.assertTrue(element.get_attribute('href')=="https://mustachematt.pythonanywhere.com/register")
        driver.find_element_by_link_text("Sign Up").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(driver.current_url=="https://mustachematt.pythonanywhere.com/mynotes")











    def test_7HomePageAfterSignin(self):
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            r=requests.head(link.get_attribute('href'))
            print(r.status_code==200)
            if r.status_code!=200:
                print(r.status_code)

        driver.get('https://mustachematt.pythonanywhere.com/homepage')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Sign Up":
                element=link
        self.assertTrue(element.get_attribute('href')=="https://mustachematt.pythonanywhere.com/register")
        driver.find_element_by_link_text("Sign Up").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(driver.current_url=="https://mustachematt.pythonanywhere.com/mynotes")


        driver.get('https://mustachematt.pythonanywhere.com/homepage')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Account":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/account")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Account").click()
        page=driver.page_source
        txt=re.search(r'Account Page',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/homepage')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="My Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/mynotes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("My Notes").click()
        page=driver.page_source
        txt=re.search(r'What would you like',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        
        driver.get('https://mustachematt.pythonanywhere.com/homepage')
        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="Delete Notes":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/delete-notes")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("Delete Notes").click()
        page=driver.page_source
        txt=re.search(r'Delete All Notes',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)

        links = driver.find_elements_by_css_selector("a")
        for link in links:
            if link.text=="":
                element3=link
        self.assertTrue(element3.get_attribute('href')=="https://mustachematt.pythonanywhere.com/homepage")
        elem=element3.get_attribute('href')
        driver.find_element_by_link_text("").click()
        page=driver.page_source
        txt=re.search(r'Stay on top',page)
        self.assertNotEqual(txt, None)
        self.assertTrue(elem==driver.current_url)












    def test_8Logouts(self):
        driver.get('https://mustachematt.pythonanywhere.com/delete-notes')
        driver.find_element_by_link_text("Logout").click()
        self.assertTrue("https://mustachematt.pythonanywhere.com/homepage"==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/login')
        username=driver.find_element_by_name("username")
        username.clear()
        username.send_keys("test1")
        password=driver.find_element_by_name("password")
        password.clear()
        password.send_keys("qwerty")
        driver.find_element_by_name("submit").click()
        driver.get('https://mustachematt.pythonanywhere.com/mynotes')
        driver.find_element_by_link_text("Logout").click()
        self.assertTrue("https://mustachematt.pythonanywhere.com/homepage"==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/login')
        username=driver.find_element_by_name("username")
        username.clear()
        username.send_keys("test1")
        password=driver.find_element_by_name("password")
        password.clear()
        password.send_keys("qwerty")
        driver.find_element_by_name("submit").click()
        driver.get('https://mustachematt.pythonanywhere.com/account')
        driver.find_element_by_link_text("Logout").click()
        self.assertTrue("https://mustachematt.pythonanywhere.com/homepage"==driver.current_url)

        driver.get('https://mustachematt.pythonanywhere.com/login')
        username=driver.find_element_by_name("username")
        username.clear()
        username.send_keys("test1")
        password=driver.find_element_by_name("password")
        password.clear()
        password.send_keys("qwerty")
        driver.find_element_by_name("submit").click()
        driver.get('https://mustachematt.pythonanywhere.com/homepage')
        driver.find_element_by_link_text("Logout").click()
        self.assertTrue("https://mustachematt.pythonanywhere.com/homepage"==driver.current_url)

































