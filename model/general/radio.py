from selene.support.shared import browser


def select(radio_name, value):
    browser.element(f'[type*="radio"][name*="{radio_name}"][value="{value}"]').element(
        '..'
    ).click()
