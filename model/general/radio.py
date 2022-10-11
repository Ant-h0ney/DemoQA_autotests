from selene.support.shared import browser


class Radio:
    def __init__(self, name: str):
        self.name = name

    def select(self, value):
        browser.element(
            f'[type*="radio"][name*="{self.name}"][value="{value}"]'
        ).element('..').click()
