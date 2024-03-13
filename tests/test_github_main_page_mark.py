import pytest
from selene import browser


def test_github_main_page_desktop(desktop_browser):
    if browser.config.window_width == [414, 400] and browser.config.window_height == [896, 800]:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip(reason='Skip test because needs desktop size')


def test_github_main_page_mobile(mobile_browser):
    if browser.config.window_width == [1920, 1600] and browser.config.window_height == [1080, 900]:
        browser.open('/')
        browser.element('[class="flex-1"] [data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in"]'). \
            click()
    else:
        pytest.skip(reason='Skip test because needs mobile size')
