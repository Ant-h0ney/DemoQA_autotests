import allure
from selene.support.shared import browser

from data import User
from model.pages import practice_form


def test_fill_successful_form():
    browser.config.hold_browser_open = True

    practice_form.open_and_clear_ads()
    with allure.step('Fill the form'):
        practice_form.fill_name(User.name)
        practice_form.fill_surname(User.surname)
        practice_form.fill_email(User.mail)
        practice_form.select_gender(User.gender)
        practice_form.fill_phone_number(User.phone_number)
        practice_form.type_birthdate(User.birthday)
        # practice_form.click_birthdate(User.birthday)
        practice_form.type_subjects(User.subjects)
        # practice_form.click_subjects(User.subjects)
        practice_form.choose_hobby(User.hobbies)
        practice_form.upload_picture(User.picture)
        practice_form.fill_address(User.address)
        practice_form.type_state(User.state)
        # practice_form.click_state(User.state)
        practice_form.type_city(User.city)
        # practice_form.click_city(User.city)
    practice_form.js_click_submit()

    # Проверка формы:
    practice_form.check_data_in_response(
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
