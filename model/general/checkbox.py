from selene import have
from selene.support.shared import browser


def select(name, hobby):
    browser.all(f'[for*="checkbox"][for*="{name}"]').element_by(have.text(hobby)).click()

    '''hobby_list = []
    hobby_css = {'sports': '1', 'reading': '2', 'music': '3'}
    for hobby in hobbies:
        hobby: str = hobby.lower()
        hobby_id = hobby_css[hobby]
        hobby_list.append(f'[id^="hobbies"][id$="{hobby_id}"]')
    for checkbox in hobby_list:
        browser.element(checkbox).element('..').click()'''