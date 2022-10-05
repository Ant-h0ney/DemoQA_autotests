import platform
import allure

from selene.support.shared import browser
from selenium.webdriver import Keys


@allure.step('Set birthdate {birthdate}')
def click_birthdate(birthdate: dict):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').set(birthdate['month'])
    browser.element('.react-datepicker__year-select').set(birthdate['year'])
    browser.element(
        f'[aria-label*="{birthdate["month"]} {birthdate["day"]}"][aria-label$="{birthdate["year"]}"]'
    ).click()


@allure.step('Set birthdate {birthdate}')
def type_birthdate(birthdate: dict):
    if platform.system() == 'Windows' or platform.system() == 'Linux':
        os_key = Keys.CONTROL
    else:
        os_key = Keys.COMMAND
    browser.element('#dateOfBirthInput').send_keys(os_key, 'a').type(
        f'{birthdate["day"]} {birthdate["month"]} {birthdate["year"]}'
    ).press_enter()
