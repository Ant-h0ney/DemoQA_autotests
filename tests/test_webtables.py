from selene.support.shared import browser
from selene import be

name = 'Anthony'
surname = 'Kononov'
mail = 'mail@mail.com'
age = '28'
salary = '15300'
department = 'web development'


def fill_the_form():
    browser.element('#firstName').clear().type(name)
    browser.element('#lastName').clear().type(surname)
    browser.element('#userEmail').clear().type(mail)
    browser.element('#age').clear().type(age)
    browser.element('#salary').clear().type(salary)
    browser.element('#department').clear().type(department)
    browser.element('#submit').click()


def test_add_row():
    browser.open('https://demoqa.com/webtables')
    browser.element('#addNewRecordButton').click()
    fill_the_form()


def test_edit_row():
    browser.open('https://demoqa.com/webtables')
    browser.element('#edit-record-2').click()
    fill_the_form()


def test_delete_row():
    browser.open('https://demoqa.com/webtables')
    browser.element('#delete-record-1').click()
