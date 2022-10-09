from selene import have
from selene.support.shared import browser


def type(determinant, value):  # NOQA
    browser.element(f'[id*="react-select"][id*="{determinant}-input"]').type(
        value
    ).press_enter()


def select(determinant, value):
    browser.element(f'[id*="react-select"][id*="{determinant}-input"]').type(
        value
    )
    browser.all(
        f'[id*="react-select"][id*="{determinant}-option"]'
    ).element_by(have.exact_text(value)).click()
