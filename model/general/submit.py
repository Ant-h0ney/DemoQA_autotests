from selene import command
from selene.support.shared import browser


def click():
    # browser.execute_script('document.getElementById("submit").click()')
    browser.element('#submit').perform(command.js.click)
