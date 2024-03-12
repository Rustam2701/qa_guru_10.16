import pytest
from selene import browser


@pytest.mark.parametrize('browser_manager_desktop', ['desktop'], indirect=True)
def test_github_main_page_desktop(browser_manager_desktop):
    if browser.config.window_width == 414 and browser.config.window_height == 896:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip(reason='Skip test because needs desktop size')


@pytest.mark.parametrize('browser_manager_mobile', ['mobile'], indirect=True)
def test_github_main_page_mobile(browser_manager_mobile):
    if browser.config.window_width == 1920 and browser.config.window_height == 1080:
        browser.open('/')
        browser.element('[class="flex-1"] [data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in"]'). \
            click()
    else:
        pytest.skip(reason='Skip test because needs mobile size')
