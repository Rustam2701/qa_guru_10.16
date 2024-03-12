import pytest
from selene import browser


@pytest.mark.parametrize('browser_manager_desktop', ['desktop'], indirect=True)
def test_github_main_page_desktop(browser_manager_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize('browser_manager_mobile', ['mobile'], indirect=True)
def test_github_main_page_mobile(browser_manager_mobile):
    browser.open('/')
    browser.element('[class="flex-1"] [data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in"]'). \
        click()
