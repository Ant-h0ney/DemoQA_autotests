from selene.support.shared import browser

from data import User
from model import app


def test_stepobject():
    browser.config.hold_browser_open = True
    app.sign_up.new_user()


def test_fluent_pageobject():
    browser.config.hold_browser_open = True
    (
        app.practice_form.open_and_clear_ads()
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
