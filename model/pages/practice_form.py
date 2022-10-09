import os
import platform

import allure
from selene import have, command
from selene.support.shared import browser
from selenium.webdriver import Keys

from model.general import radio, checkbox, dropdown
from tests.Practice_form.data import User


@allure.step('Open an url from mainpage "/automation-practice-form"')
def open_and_clear_ads():
    browser.open_url('/automation-practice-form')
    ads = browser.all('[id^=google_ads][id*=container]')
    if ads.with_(timeout=6).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


@allure.step('Click on gender button {gender}')
def select_gender(gender: str, radio_name='gender'):
    radio.select(radio_name, gender)


@allure.step('Click on checkboxes of hobby {hobbies}')
def choose_hobby(hobbies: User.hobbies, checkbox_name='hobbies'):
    for hobby in hobbies:
        checkbox.select(checkbox_name, hobby)


@allure.step('Set state {state}')
def type_state(state: str, dropdown_state='3'):
    dropdown.type(dropdown_state, state)


@allure.step('Set state {state}')
def click_state(state: str, dropdown_state=3):
    dropdown.select(dropdown_state, state)


@allure.step('Set city {city}')
def type_city(city: str, dropdown_city=4):
    dropdown.type(dropdown_city, city)


@allure.step('Set city {city}')
def click_city(city: str, dropdown_city=4):
    dropdown.select(dropdown_city, city)


@allure.step('Validate responsive data {args}')
def check_data_in_response(*args):
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


@allure.step('Set address {address}')
def fill_address(address: str):
    browser.element('#currentAddress').type(address)


@allure.step('Set name {name}')
def fill_name(name: str):
    browser.element('#firstName').type(name)


@allure.step('Set surname {surname}')
def fill_surname(surname: str):
    browser.element('#lastName').type(surname)


@allure.step('Set email {email}')
def fill_email(email: str):
    browser.element('#userEmail').type(email)


@allure.step('Set mobile {phone_number}')
def fill_phone_number(phone_number):
    browser.element('#userNumber').type(phone_number)


@allure.step('Set birthdate {birthdate}')
def click_birthdate(birthdate: dict):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').set(birthdate['month'])
    browser.element('.react-datepicker__year-select').set(birthdate['year'])
    browser.element(
        f'[aria-label*="{birthdate["month"]} {birthdate["day"]}"][aria-label$="{birthdate["year"]}"]'
    ).click()


@allure.step('Set birthdate {birthdate}')
def type_birthdate(birthdate: dict):
    if platform.system() == 'Windows' or platform.system() == 'Linux':
        os_key = Keys.CONTROL
    else:
        os_key = Keys.COMMAND
    browser.element('#dateOfBirthInput').send_keys(os_key, 'a').type(
        f'{birthdate["day"]} {birthdate["month"]} {birthdate["year"]}'
    ).press_enter()


@allure.step('Set subjects {subjects}')
def set_by_typing(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}').press_enter()


@allure.step('Set subjects {subjects}')
def set_by_clicking(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}')
        browser.element('[id^="react-select-2"]').click()


@allure.step('Upload a picture {filename}')
def picture(filename):
    working_dir_path = os.path.abspath('')
    picture_path = os.path.join(working_dir_path, filename)
    browser.element('#uploadPicture').send_keys(picture_path)


@allure.step('Click on the submit button')
def js_click():
    # browser.execute_script('document.getElementById("submit").click()')
    browser.element('#submit').perform(command.js.click)
