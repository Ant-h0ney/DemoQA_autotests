import allure
from selene.support.shared import browser


@allure.step('Set address {address}')
def fill_address(address: str):
    browser.element('#currentAddress').type(address)


@allure.step('Set name {name}')
def fill_name(name: str):
    browser.element('#firstName').type(name)


@allure.step('Set surname {surname}')
def fill_surname(surname: str):
    browser.element('#lastName').type(surname)


@allure.step('Set email {email}')
def fill_email(email: str):
    browser.element('#userEmail').type(email)


@allure.step('Set mobile {phone_number}')
def fill_phone_number(phone_number):
    browser.element('#userNumber').type(phone_number)
