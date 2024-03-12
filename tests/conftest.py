import pytest
from selene import browser


@pytest.fixture(params=['desktop'], scope='function')
def browser_manager_desktop(request):
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(params=['mobile'], scope='function')
def browser_manager_mobile(request):
    browser.config.base_url = 'https://github.com/'
    browser.config.window_width = 414
    browser.config.window_height = 896

    yield

    browser.quit()
