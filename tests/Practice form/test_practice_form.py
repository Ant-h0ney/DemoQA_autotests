import model.general
from model.pages import practice_form
from data import User


def test_fill_successful_form():
    practice_form.open_page()
    model.general.forms.fill_name(User.name)
    model.general.forms.fill_surname(User.surname)
    model.general.forms.fill_email(User.mail)
    practice_form.click_gender_radio(User.gender)
    model.general.forms.fill_phone_number(User.phone_number)
    model.general.datepicker.set_by_type(User.birthday)
    # model.general.datepicker.set_by_click(User.birthday)
    model.general.subject.set_by_typing(User.subjects)
    # model.general.subject.set_by_clicking(User.subjects)
    practice_form.set_hobbies(User.hobbies)
    model.general.upload.picture(User.picture)
    model.general.forms.fill_address(User.address)
    practice_form.set_state_by_typing(User.state)
    # practice_form.set_state_by_clicking(User.state)
    practice_form.set_city_by_typing(User.city)
    # practice_form.set_city_by_clicking(User.city)
    model.general.submit.click()

    # Проверка формы:
    practice_form.check_the_table(
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
