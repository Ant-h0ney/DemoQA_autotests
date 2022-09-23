from selene.support.shared import browser


def open_page():
    browser.open_url('/automation-practice-form')


def click_gender_radio(gender: str):
    gender_lowcap = gender.lower().capitalize()
    gender_element = f'[id^="gender"][value="{gender_lowcap}"]'
    browser.element(gender_element).parent_element.click()


def set_hobbies(hobbies: tuple):
    hobby_list = []
    hobby_css = {'sports': '1', 'reading': '2', 'music': '3'}
    for hobby in hobbies:
        hobby: str = hobby.lower()
        hobby_id = hobby_css[hobby]
        hobby_list.append(f'[id^="hobbies"][id$="{hobby_id}"]')
    for checkbox in hobby_list:
        browser.element(checkbox).parent_element.click()


def set_state_by_typing(state: str):
    browser.element('#react-select-3-input').type(state).press_enter()


def set_state_by_clicking(state: str):
    browser.element('#react-select-3-input').type(state)
    browser.element('[id^="react-select-3-option"]').click()


def set_city_by_typing(city):
    browser.element('#react-select-4-input').type(city).press_enter()


def set_city_by_clicking(city):
    browser.element('#react-select-4-input').type(city)
    browser.element('[id^="react-select-4-option"]').click()


