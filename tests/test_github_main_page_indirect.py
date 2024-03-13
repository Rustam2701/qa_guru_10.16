import pytest
from selene import browser


@pytest.mark.parametrize('desktop_browser', [(1920, 1080), (1600, 900)], indirect=True)
def test_github_main_page_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('mobile_browser', [(896, 414), (800, 400)], indirect=True)
def test_github_main_page_mobile(mobile_browser):
    browser.open('/')
    browser.element('[class="flex-1"] [data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in"]'). \
        click()

