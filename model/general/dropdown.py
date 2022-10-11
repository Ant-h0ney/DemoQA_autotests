from selene import have
from selene.support.shared import browser


class Dropdown:
    def __init__(self, name: str):
        self.name = name

    def type(self, value):  # NOQA
        browser.element(f'[id*="react-select"][id*="{self.name}-input"]').type(
            value
        ).press_enter()

    def select(self, value):
        browser.element(f'[id*="react-select"][id*="{self.name}-input"]').type(value)
        browser.all(f'[id*="react-select"][id*="{self.name}-option"]').element_by(
            have.exact_text(value)
        ).click()
