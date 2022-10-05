import platform

import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import model


# def pytest_add_addoption(parser):
#     parser.addoption()


@pytest.fixture(scope='function', autouse=True)
def browser_preparation(attachments):
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config.window_height = 1000
    browser.config.base_url = 'https://demoqa.com'
    if platform.system() != 'Windows':
        options = Options()
        selenoid_capabilities = {
            'browserName': 'chrome',
            'browserVersion': '100.0',
            'selenoid:options': {'enableVNC': True, 'enableVideo': True},
        }
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor='https://user1:1234@selenoid.autotests.cloud/wd/hub',
            options=options,
        )
        browser.config.driver = driver
    yield


@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)
    yield


@pytest.fixture(scope='function')
def attachments():
    yield
    model.utils.allure.attach.screenshot()
    model.utils.allure.attach.logs()
    model.utils.allure.attach.html()
    if platform.system() != 'Windows':
        model.utils.allure.attach.video()
    browser.quit()
