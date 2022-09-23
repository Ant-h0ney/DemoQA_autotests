import os
from selene.support.shared import browser
from selene import have
import model.general.forms as forms
from model.pages import practice_form

name = 'Anthony'
surname = 'Kononov'
mail = 'mail@mail.com'
gender = 'feMale'  # Male/Female/Other
phone_number = '0123456789'  # must be 10-digit
# birthday = {'day': '28', 'month': 'March', 'Year': '1995'}
month = 'March'
day = '17'
year = '1995'
subjects = ('Math', 'Chemistry')
hobbies = ('SpOrtS', 'rEaDiNG')  # Sports/Reading/Music
picture_path = os.path.join(os.path.abspath(''), 'Practice form', 'photo.jpg')
address = 'bigadress a lot of letters inside string'
state = 'HaryAna'
city = 'KarnaL'
'''
#     [{'state': 'NCR', 'city': ['Delhi', 'Guargon', 'Noida']},
#     {'state': 'Uttar Pradesh', 'city': ['Agra', 'Lucknow', 'Merrut']},
#     {'state': 'Haryana', 'city': ['Karnal', 'Panipat']},
#     {'state': 'Rajasthan', 'city': ['Jaipur', 'Jaiselmer']}]
'''


def test_fill_successful_form():
    # browser.config.hold_browser_open = True
    practice_form.open_page()
    forms.fill_name(name)
    forms.fill_surname(surname)
    forms.fill_email(mail)
    practice_form.click_gender_radio(gender)
    forms.fill_phone_number(phone_number)
    forms.choose_birthdate_by_clicking(day, month, year)
    # practice_form.choose_birthdate_by_typing(day, month, year)
    # forms.set_subjects_by_typing(subjects)
    forms.set_subjects_by_clicking(subjects)
    practice_form.set_hobbies(hobbies)
    forms.upload_picture(picture_path)
    forms.fill_address(address)
    # practice_form.set_state_by_typing(state)
    practice_form.set_state_by_clicking(state)
    # practice_form.set_city_by_typing(city)
    practice_form.set_city_by_clicking(city)
    forms.click_on_submit()

    # Проверка формы:
    # Обернуть бы модуль проверок лаконично, красиво, и чтобы понятно было где валится. Пока слишком деревянно
    browser.all('.table-responsive').should(have.text(f'{name}'))
    browser.all('.table-responsive').should(have.text(f'{surname}'))
    browser.all('.table-responsive').should(have.text(f'{mail}'))
    browser.all('.table-responsive').should(have.text(f'{gender.lower().capitalize()}'))
    browser.all('.table-responsive').should(have.text(f'{phone_number}'))
    browser.all('.table-responsive').should(have.text(f'{day} {month},{year}'))
    for subject in subjects:
        browser.all('.table-responsive').should(have.text(f'{subject.lower().capitalize()}'))
    for hobby in hobbies:
        browser.all('.table-responsive').should(have.text(f'{hobby.lower().capitalize()}'))
    # browser.all('.table-responsive').should(have.text(f'{picture}'))
    browser.all('.table-responsive').should(have.text(f'{address}'))
    browser.all('.table-responsive').should(have.text(f'{state.lower().capitalize()}'))
    browser.all('.table-responsive').should(have.text(f'{city.lower().capitalize()}'))
