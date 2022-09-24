import model
from model.pages import practice_form

name = 'Anthony'
surname = 'Kononov'
mail = 'mail@mail.com'
gender = 'Female'  # Male/Female/Other
phone_number = '0123456789'  # must be 10-digit
birthday = {'day': '28', 'month': 'March', 'year': '1995'}
subjects = ('Math', 'Chemistry')
hobbies = ('Sports', 'Reading')  # Sports/Reading/Music
picture = 'photo.jpg'
address = 'bigadress a lot of letters inside string'
state = 'Haryana'
city = 'Karnal'
'''
#     [{'state': 'NCR', 'city': ['Delhi', 'Guargon', 'Noida']},
#     {'state': 'Uttar Pradesh', 'city': ['Agra', 'Lucknow', 'Merrut']},
#     {'state': 'Haryana', 'city': ['Karnal', 'Panipat']},
#     {'state': 'Rajasthan', 'city': ['Jaipur', 'Jaiselmer']}]
'''


def test_fill_successful_form():
    practice_form.open_page()
    model.general.forms.fill_name(name)
    model.general.forms.fill_surname(surname)
    model.general.forms.fill_email(mail)
    practice_form.click_gender_radio(gender)
    model.general.forms.fill_phone_number(phone_number)
    model.general.forms.choose_birthdate_by_typing(birthday)
    # model.general.forms.choose_birthdate_by_clicking(birthday)
    model.general.forms.set_subjects_by_typing(subjects)
    # model.general.forms.set_subjects_by_clicking(subjects)
    practice_form.set_hobbies(hobbies)
    model.general.forms.upload_picture(picture)
    model.general.forms.fill_address(address)
    practice_form.set_state_by_typing(state)
    # practice_form.set_state_by_clicking(state)
    practice_form.set_city_by_typing(city)
    # practice_form.set_city_by_clicking(city)
    model.general.forms.click_on_submit()

    # Проверка формы:
    practice_form.check_the_table(
        name,
        surname,
        mail,
        gender,
        phone_number,
        birthday,
        subjects,
        hobbies,
        picture,
        address,
        state,
        city,
    )
