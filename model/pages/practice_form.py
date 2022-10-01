import allure
from selene import have, command
from selene.support.shared import browser


@allure.step('Open an url from mainpage {url}')
def open_page(url):
    browser.open_url(url)
    ads = browser.all('[id^=google_ads][id*=container]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


@allure.step('Click on gender button {gender}')
def choose_gender(gender: str):
    gender_lowcap = gender.lower().capitalize()
    gender_element = f'[id^="gender"][value="{gender_lowcap}"]'
    browser.element(gender_element).parent_element.click()


@allure.step('Click on checkboxes of hobby {hobbies}')
def choose_hobby(hobbies: tuple):
    hobby_list = []
    hobby_css = {'sports': '1', 'reading': '2', 'music': '3'}
    for hobby in hobbies:
        hobby: str = hobby.lower()
        hobby_id = hobby_css[hobby]
        hobby_list.append(f'[id^="hobbies"][id$="{hobby_id}"]')
    for checkbox in hobby_list:
        browser.element(checkbox).parent_element.click()


@allure.step('Set state {state}')
def type_state(state: str):
    browser.element('#react-select-3-input').type(state).press_enter()


@allure.step('Set state {state}')
def click_state(state: str):
    browser.element('#react-select-3-input').type(state)
    browser.element('[id^="react-select-3-option"]').click()


@allure.step('Set city {city}')
def type_city(city):
    browser.element('#react-select-4-input').type(city).press_enter()


@allure.step('Set city {city}')
def click_city(city):
    browser.element('#react-select-4-input').type(city)
    browser.element('[id^="react-select-4-option"]').click()


@allure.step('Validate responsive table {args}')
def check_the_table(*args, **kwargs):
    for value in args:
        if type(value) == str:
            browser.all('.table-responsive').should(have.text(f'{value}'))
        if type(value) == tuple:
            for elem in value:
                browser.all('.table-responsive').should(have.text(f'{elem}'))
        if type(value) == dict:
            browser.all('.table-responsive').should(
                have.text(f'{value["day"]} {value["month"]},{value["year"]}')
            )
    # непойму, почему через кваргу не получается
    # for birthdate in kwargs:
    #     browser.all('.table-responsive')\
    #         .should(have.text(f'{birthdate[0]} {birthdate[1]},{birthdate[2]}'))
