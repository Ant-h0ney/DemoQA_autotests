import allure
import pytest
from allure_commons.types import AttachmentType
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_preparation():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1000
    browser.config.window_height = 800
    browser.config.base_url = 'https://demoqa.com'
    yield


@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    monkeypatch.chdir(request.fspath.dirname)
    yield


''' It deserve to exist. But must be improved (cuz a lot of lines at Allure)
@pytest.fixture(autouse=True)
def screenshot():
    yield
    screen = browser.driver.get_screenshot_as_png()
    allure.attach(
        screen,
        name='screenshot',
        attachment_type=AttachmentType.PNG,
    )


@pytest.fixture(autouse=True)
def logs():
    yield
    logfile = ''.join(
        f'{text}\n' for text in browser.driver.get_log(log_type='browser')
    )
    allure.attach(
        logfile,
        name='browser_log',
        attachment_type=AttachmentType.TEXT,
    )


@pytest.fixture(autouse=True)
def html():
    yield
    source = browser.driver.page_source
    allure.attach(
        source,
        name='HTML',
        attachment_type=AttachmentType.HTML,
    )
'''
