from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

@given(u'"username" field is empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given "username" field is empty')


@when(u'I click the Sign In button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the Sign In button')


@then(u'I see a "This field is required" "nameError"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see a "This field is required" "nameError"')


@given(u'"password" field is empty')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given "password" field is empty')


@when(u'I click on the "Sign In" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the "Sign In" button')



@then(u'I see a "This field is required" "passwordError"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I see a "This field is required" "passwordError"')