from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

@given(u'I am on "{url}"')
def step_impl(context,url):
    context.browser = webdriver.Chrome()
    context.browser.get(url)

@given(u'I see "{title}" in the title')
def step_impl(context, title):
    assert title in context.browser.title


@when(u'I click the "{login_button}"')
def step_impl(context, login_button):
    context.browser.find_element_by_id(login_button).click()

@then(u'I should be on the "{title}" page')
def step_imp(context, title):
        assert title in context.browser.title

@then(u'I should see the "{element}"')
def step_impl(context, element):
    assert element in context.browser.page_source