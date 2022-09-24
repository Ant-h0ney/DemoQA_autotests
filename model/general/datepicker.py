import platform

from selene.support.shared import browser
from selenium.webdriver import Keys


def set_by_click(birthdate: dict):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(birthdate['month'])
    browser.element('.react-datepicker__year-select').type(birthdate['year'])
    browser.element(
        f'[aria-label*="{birthdate["month"]} {birthdate["day"]}"][aria-label$="{birthdate["year"]}"]'
    ).click()


def set_by_type(birthdate: dict):
    if platform.system() == 'Windows':
        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type(
            f'{birthdate["day"]} {birthdate["month"]} {birthdate["year"]}'
        ).press_enter()
    else:
        browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND, 'a').type(
            f'{birthdate["day"]} {birthdate["month"]} {birthdate["year"]}'
        ).press_enter()
