from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep

#scenario: verify error for empty username field

@given(u'"{f}" field is empty')
def step_impl(context,f):
    #empty string are falsy so assert not false so that its true
    #put in --no-capture on the comand line to see print statements
    print("text in field:" + context.browser.find_element_by_id(f).get_attribute('value'))
    assert not context.browser.find_element_by_id(f).get_attribute('value')

@when(u'I click on the Sign In button')
def step_impl(context):
    context.browser.find_element_by_name("submit").click()
    #can be used for a text field to click enter afterwards
    #context.browser.find_element_by_name("value").send_keys(Keys.RETURN)

@then(u'I see a "{error}" in "{field}"')
def step_impl(context,error,field):
    #field = context.browser.find_element_by_name(field).get_attribute("innerHTML")
    assert error in context.browser.find_element_by_name(field).get_attribute("innerHTML")


#use username test password test
@given(u'we type in "{t}" in the "{f}" field')
def step_impl(context, t, f):
    context.browser.find_element_by_name(f).send_keys(t)


#schenario remember me button
@given(u'I click on "{f}" field')
def step_impl(context,f):
    context.browser.find_element_by_name(f).click()

@then(u'I click on the Sign In button')
def step_impl(context):
    context.browser.find_element_by_name("submit").click()


@then(u'Close the browser')
def step_impl(context):
    context.browser.close()
    #driver = webdriver.Chrome()


@given(u'I navigate to "{url}"')
def step_impl(context,url):
    
    #context.browser=webdriver.Chrome()
    context.browser.get(url)