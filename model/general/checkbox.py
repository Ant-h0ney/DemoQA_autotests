from selene import have
from selene.support.shared import browser


def select(checkbox_name, *args):
    for value in args:
        browser.all(f'[for*="checkbox"][for*="{checkbox_name}"]').element_by(have.text(value)).click()
