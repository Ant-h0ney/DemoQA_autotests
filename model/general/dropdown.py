from selene import have
from selene.support.shared import browser


def type(dropdown_determinant, value):  # NOQA
    browser.element(f'[id*="react-select"][id*="{dropdown_determinant}-input"]').type(
        value
    ).press_enter()


def select(dropdown_determinant, value):
    browser.element(f'[id*="react-select"][id*="{dropdown_determinant}-input"]').type(
        value
    )
    browser.all(
        f'[id*="react-select"][id*="{dropdown_determinant}-option"]'
    ).element_by(have.exact_text(value)).click()
