import platform

from selene.support.shared import browser
from selenium.webdriver import Keys


def choose(date: dict):
    browser.element('[class*="react-datepicker"]').click()
    browser.element('.react-datepicker__month-select').send_keys(date['month'])
    browser.element('.react-datepicker__year-select').send_keys(date['year'])
    browser.element(
        f'[aria-label*="{date["month"]} {date["day"]}"][aria-label$="{date["year"]}"]'
    ).click()


def type(date: dict):  # NOQA
    if platform.system() == 'Windows' or platform.system() == 'Linux':
        os_key = Keys.CONTROL
    else:
        os_key = Keys.COMMAND
    browser.element('#dateOfBirthInput').send_keys(os_key, 'a').type(
        f'{date["day"]} {date["month"]} {date["year"]}'
    ).press_enter()
