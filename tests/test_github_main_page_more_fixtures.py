import pytest
from selene import browser


def test_github_main_page_desktop(desktop_browser):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_main_page_mobile(mobile_browser):
    browser.open('/')
    browser.element('[class="flex-1"] [data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in"]'). \
        click()
