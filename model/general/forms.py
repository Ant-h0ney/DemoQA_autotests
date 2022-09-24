import os
import platform

from selene import command
from selene.support.shared import browser
from selenium.webdriver import Keys


def upload_picture(picture):
    working_dir_path = os.path.abspath('')
    picture_path = os.path.join(working_dir_path, picture)
    browser.element('#uploadPicture').send_keys(picture_path)


def click_on_submit():
    # browser.execute_script('document.getElementById("submit").click()')
    browser.element('#submit').perform(command.js.click)


def fill_address(address: str):
    browser.element('#currentAddress').type(address)


def choose_birthdate_by_clicking(birthdate: dict):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(birthdate['month'])
    browser.element('.react-datepicker__year-select').type(birthdate['year'])
    browser.element(
        f'[aria-label*="{birthdate["month"]} {birthdate["day"]}"][aria-label$="{birthdate["year"]}"]'
    ).click()


def choose_birthdate_by_typing(birthdate: dict):
    if platform.system() == 'Windows':
        browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type(
            f'{birthdate["day"]} {birthdate["month"]} {birthdate["year"]}'
        ).press_enter()
    else:
        browser.element('#dateOfBirthInput').send_keys(Keys.COMMAND, 'a').type(
            f'{birthdate["day"]} {birthdate["month"]} {birthdate["year"]}'
        ).press_enter()


def fill_name(name: str):
    browser.element('#firstName').type(name)


def fill_surname(surname: str):
    browser.element('#lastName').type(surname)


def fill_email(email: str):
    browser.element('#userEmail').type(email)


def fill_phone_number(phone_number):
    browser.element('#userNumber').type(phone_number)


def set_subjects_by_typing(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}').press_enter()


def set_subjects_by_clicking(subjects: tuple):
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}')
        browser.element('[id^="react-select-2"]').click()
