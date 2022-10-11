import platform

from selene.support.shared import browser
from selenium.webdriver import Keys


class DatePicker:
    def __init__(self, name: str):
        self.name = name

    def choose(self, date: dict):
        browser.element(f'#dateOf{self.name}Input').click()
        browser.element('[class*="month-select"]').send_keys(date['month'])
        browser.element('[class*="month-select"]').send_keys(date['year'])
        browser.element(
            f'[aria-label*="{date["month"]} {date["day"]}"][aria-label$="{date["year"]}"]'
        ).click()

    def type(self, date: dict):  # NOQA
        if platform.system() == 'Windows' or platform.system() == 'Linux':
            os_key = Keys.CONTROL
        else:
            os_key = Keys.COMMAND
        browser.element(f'#dateOf{self.name}Input').send_keys(os_key, 'a').type(
            f'{date["day"]} {date["month"]} {date["year"]}'
        ).press_enter()
