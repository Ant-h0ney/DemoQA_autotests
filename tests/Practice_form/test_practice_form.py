import model
from data import User


def test_fill_successful_form():
    model.pages.practice_form.open_and_clear_ads()
    model.general.forms.fill_name(User.name)
    model.general.forms.fill_surname(User.surname)
    model.general.forms.fill_email(User.mail)
    model.pages.practice_form.choose_gender(User.gender)
    model.general.forms.fill_phone_number(User.phone_number)
    model.general.datepicker.type_birthdate(User.birthday)
    # model.general.datepicker.click_birthdate(User.birthday)
    model.general.subject.set_by_typing(User.subjects)
    # model.general.subject.set_by_clicking(User.subjects)
    model.pages.practice_form.choose_hobby(User.hobbies)
    model.general.upload.picture(User.picture)
    model.general.forms.fill_address(User.address)
    model.pages.practice_form.type_state(User.state)
    # model.pages.practice_form.click_state(User.state)
    model.pages.practice_form.type_city(User.city)
    # model.pages.practice_form.click_city(User.city)
    model.general.submit.js_click()

    # Проверка формы:
    model.pages.practice_form.check_data_in_response(
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
