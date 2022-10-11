import allure
from selene import have, command
from selene.support.shared import browser

from model.general.checkbox import Checkbox
from model.general.datepicker import DatePicker
from model.general.dropdown import Dropdown
from model.general.radio import Radio
from model.general.upload import Upload
from tests.Practice_form.data import User


class PracticeForm:
    def __init__(self):
        self._radio = 'gender'
        self._checkbox = 'hobbies'
        self._dropdown_state = '3'
        self._dropdown_city = '4'
        self._datepicker_name = 'Birth'
        self._type_of_file = 'Picture'
        self._subject = '#subjectsInput'

    @allure.step('Open an url from mainpage "/automation-practice-form"')
    def open_and_clear_ads(self):
        browser.open('/automation-practice-form')
        ads = browser.all('[id^=google_ads][id*=container]')
        if ads.with_(timeout=6).wait.until(have.size_greater_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self

    @allure.step('Click on gender button {gender}')
    def select_gender(self, gender: str):
        Radio(self._radio).select(gender)
        return self

    @allure.step('Click on checkboxes of hobby {hobbies}')
    def choose_hobby(self, hobbies: User.hobbies):
        for hobby in hobbies:
            Checkbox(self._checkbox).select(hobby)
        return self

    @allure.step('Set state {state}')
    def type_state(self, state: str):
        Dropdown(self._dropdown_state).type(state)
        return self

    @allure.step('Set state {state}')
    def click_state(self, state: str):
        Dropdown(self._dropdown_state).select(state)
        return self

    @allure.step('Set city {city}')
    def type_city(self, city: str):
        Dropdown(self._dropdown_city).type(city)
        return self

    @allure.step('Set city {city}')
    def click_city(self, city: str):
        Dropdown(self._dropdown_city).select(city)
        return self

    @allure.step('Set address {address}')
    def fill_address(self, address: str):
        browser.element('#currentAddress').type(address)
        return self

    @allure.step('Set name {name}')
    def fill_name(self, name: str):
        browser.element('#firstName').type(name)
        return self

    @allure.step('Set surname {surname}')
    def fill_surname(self, surname: str):
        browser.element('#lastName').type(surname)
        return self

    @allure.step('Set email {email}')
    def fill_email(self, email: str):
        browser.element('#userEmail').type(email)
        return self

    @allure.step('Set mobile {phone_number}')
    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').type(phone_number)
        return self

    @allure.step('Set birthdate {birthdate}')
    def click_birthdate(self, birthdate: dict):
        DatePicker(self._datepicker_name).choose(birthdate)
        return self

    @allure.step('Set birthdate {birthdate}')
    def type_birthdate(self, birthdate: dict):
        DatePicker(self._datepicker_name).type(birthdate)
        return self

    @allure.step('Set subjects {subjects}')
    def type_subjects(self, subjects: tuple):
        for subject in subjects:
            browser.element(self._subject).click().type(f'{subject}').press_enter()
        return self

    @allure.step('Set subjects {subjects}')
    def click_subjects(self, subjects: tuple):
        for subject in subjects:
            browser.element(self._subject).click().type(f'{subject}')
            browser.element('[id^="react-select-2"]').click()
        return self

    @allure.step('Upload a picture {filename}')
    def upload_picture(self, filename):
        Upload(self._type_of_file).file(filename)
        return self

    @allure.step('Click on the submit button')
    def js_click_submit(self):
        browser.element('#submit').perform(command.js.click)
        return self

    @allure.step('Validate responsive data {args}')
    def check_data_in_response(self, *args):
        for value in args:
            if type(value) == str:
                browser.element('.modal-content').all('table tbody tr').all(
                    'td'
                ).element_by(have.text(f'{value}')).should(have.text(f'{value}'))
            if type(value) == tuple:
                for elem in value:
                    browser.element('.modal-content').all('table tbody tr').all(
                        'td'
                    ).element_by(have.text(f'{elem}')).should(have.text(f'{elem}'))
            if type(value) == dict:
                browser.element('.modal-content').all('table tbody tr').all(
                    'td'
                ).element_by(
                    have.text(f'{value["day"]} {value["month"]},{value["year"]}')
                ).should(
                    have.text(f'{value["day"]} {value["month"]},{value["year"]}')
                )


class Registration:
    def __init__(self):
        self._makesomemagic = PracticeForm()

    def new_user(self):
        (
            self._makesomemagic.open_and_clear_ads()
            .fill_name(User.name)
            .fill_surname(User.surname)
            .fill_email(User.mail)
            .select_gender(User.gender)
            .fill_phone_number(User.phone_number)
            .type_birthdate(User.birthday)
            .type_subjects(User.subjects)
            .choose_hobby(User.hobbies)
            .upload_picture(User.picture)
            .fill_address(User.address)
            .type_state(User.state)
            .type_city(User.city)
            .js_click_submit()
            .check_data_in_response(
                User.name,
                User.surname,
                User.mail,
                User.gender,
                User.phone_number,
                User.birthday,
                User.subjects,
                User.hobbies,
                User.picture,
                User.address,
                User.state,
                User.city,
            )
        )
