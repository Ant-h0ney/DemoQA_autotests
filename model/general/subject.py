import allure
from selene.support.shared import browser


@allure.step('Set subjects {subjects}')
def set_by_typing(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}').press_enter()


@allure.step('Set subjects {subjects}')
def set_by_clicking(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}')
        browser.element('[id^="react-select-2"]').click()
