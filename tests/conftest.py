import pytest
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
