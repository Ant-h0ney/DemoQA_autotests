from selene.support.shared import browser


def fill_address(address: str):
    browser.element('#currentAddress').type(address)


def fill_name(name: str):
    browser.element('#firstName').type(name)


def fill_surname(surname: str):
    browser.element('#lastName').type(surname)


def fill_email(email: str):
    browser.element('#userEmail').type(email)


def fill_phone_number(phone_number):
    browser.element('#userNumber').type(phone_number)
