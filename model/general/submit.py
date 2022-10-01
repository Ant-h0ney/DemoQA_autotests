import allure
from selene import command
from selene.support.shared import browser


@allure.step('Click on the submit button')
def js_click():
    # browser.execute_script('document.getElementById("submit").click()')
    browser.element('#submit').perform(command.js.click)
