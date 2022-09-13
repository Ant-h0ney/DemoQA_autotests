import os

from selene.support.shared import browser
from selene import be

name = 'Anthony'
surname = 'Kononov'
mail = 'mail@mail.com'
gender = 'Male'  # Male/Female/Other
phone_number = '0123456789'  # must be 10-digit
# birthday = {'day': '28', 'month': 'March', 'Year': '1995'}
month = 'March'
day = '17'
year = '1995'
subjects = ['Math', 'Chemistry']
hobbies = ['Sports', 'rEaDiNG']  # Sports/Reading/Music
address = 'bigadress a lot of letters inside string'
state = 'Haryana'
city = 'Karnal'
filepath = 'photo.jpg'
# В идеале сделать самоопределение штата, при выборе корректного города
#     [{'state': 'NCR', 'city': ['Delhi', 'Guargon', 'Noida']},
#     {'state': 'Uttar Pradesh', 'city': ['Agra', 'Lucknow', 'Merrut']},
#     {'state': 'Haryana', 'city': ['Karnal', 'Panipat']},
#     {'state': 'Rajasthan', 'city': ['Jaipur', 'Jaiselmer']}]


def gender_button():
    if gender.lower() == 'male':
        gender_button = '#gender-radio-1'
        return gender_button
    elif gender.lower() == 'female':
        gender_button = '#gender-radio-2'
        return gender_button
    elif gender.lower() == 'other':
        gender_button = '#gender-radio-3'
        return gender_button
    # чтобы не сломать тест, если неверно введён пол
    else:
        gender_button = '#gender-radio-1'
        return gender_button


def hobbies_checkbox():
    hobby_list = []
    for hobby in hobbies:
        if hobby.lower() == 'sports':
            hobby_list.append('#hobbies-checkbox-1')
        if hobby.lower() == 'reading':
            hobby_list.append('#hobbies-checkbox-2')
        if hobby.lower() == 'music':
            hobby_list.append('#hobbies-checkbox-3')
    return hobby_list


def test_fill_successful_form():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').should(be.blank).type(name)
    browser.element('#lastName').should(be.blank).type(surname)
    browser.element('#userEmail').should(be.blank).type(mail)
    browser.element(gender_button()).parent_element.click()
    browser.element('#userNumber').should(be.blank).type(phone_number)

    # воркэраунд, описанный при выполнении дз со(*) на первом уроке.
    # симуляция нажатия по полю, выделение всего содержимого (ctrl+a), очистка (backspace)
    # browser.element('#dateOfBirthInput').send_keys(Keys.CONTROL, 'a').type('28 Mar 1995').press_enter()

    # через JS, думаю тоже можно довести до ума, чтобы дата не откатывалась к значению по умолчанию
    # browser.execute_script(f"document.getElementById('dateOfBirthInput').value = '{birthday}'")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type(month)
    browser.element('.react-datepicker__year-select').type(year)
    # Требуется доработка, для дней рождения 1,2,3 чисел (st, nd, rd)
    browser.element(f'[aria-label$="{month} {day}th, {year}"]').click()

    browser.element('#uploadPicture').send_keys(os.getcwd()+f'./{filepath}')
    for subject in subjects:
        browser.element('#subjectsInput').click().type(f'{subject}').press_enter()
    for checkbox in hobbies_checkbox():
        browser.element(checkbox).parent_element.click()
    browser.element('#currentAddress').should(be.blank).type(address)
    browser.element('#react-select-3-input').should(be.blank).type(state).press_enter()
    browser.element('#react-select-4-input').should(be.blank).type(city).press_enter()
    browser.execute_script('document.getElementById("submit").click()')
