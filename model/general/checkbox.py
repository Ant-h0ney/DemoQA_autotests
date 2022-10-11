from selene import have
from selene.support.shared import browser


class Checkbox:
    def __init__(self, name: str):
        self.name = name

    def select(self, *args):
        for value in args:
            browser.all(f'[for*="checkbox"][for*="{self.name}"]').element_by(
                have.text(value)
            ).click()
