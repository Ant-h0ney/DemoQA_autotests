from selene.support.shared import browser
from selenium.webdriver import Keys


def upload_picture(picture_path):
    browser.element('#uploadPicture').send_keys(picture_path)


def click_on_submit():
    browser.execute_script('document.getElementById("submit").click()')


def fill_address(address: str):
    browser.element('#currentAddress').type(address)


def choose_birthdate_by_clicking(day, month, year):
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(month)
    browser.element('.react-datepicker__year-select').type(year)
    browser.element(f'[aria-label*="{month} {day}"][aria-label$="{year}"]').click()


def choose_birthdate_by_typing(day, month, year):
    browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type(f'{day} {month} {year}').press_enter()


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
