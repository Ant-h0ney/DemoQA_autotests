from selene.support.shared import browser
from selene import be, have

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
    # browser.config.hold_browser_open = True
    browser.open_url('/webtables')
    browser.element('#addNewRecordButton').click()
    fill_the_form()

    # Проверочки
    browser.all('.rt-tr-group')[3].all('.rt-td').should(have.texts(name, surname, age, mail, salary, department, ''))


def test_edit_row():
    browser.open_url('/webtables')
    browser.element('#edit-record-2').click()
    fill_the_form()

    # Проверочки
    browser.all('.rt-tr-group')[1].all('.rt-td').should(have.texts(name, surname, age, mail, salary, department, ''))


def test_delete_row():
    browser.open_url('/webtables')
    browser.element('#delete-record-1').click()

    # Проверочки
    browser.all('.rt-tr-group')[0].all('.rt-td').should(have.no.texts('Cierra', 'Vega', '39', 'cierra@example.com',
                                                                      '10000', 'Insurance', ''))
