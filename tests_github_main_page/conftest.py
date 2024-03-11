import pytest
from selene import browser

@pytest.fixture(scope='session', autouse=True)
def browser_manager():
    browser.open('https://github.com')
    browser.config.window_width = 1920
    browser.config.window_width = 1080

    yield

    browser.quit()
