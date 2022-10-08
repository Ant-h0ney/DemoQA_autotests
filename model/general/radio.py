from selene.support.shared import browser


def select(name, value):
    browser.element(f'[type*="radio"][name*="{name}"][value="{value}"]').element(
        '..'
    ).click()
