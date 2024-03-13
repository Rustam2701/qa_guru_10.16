import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1600, 900), (800, 400), (896, 414)])
def desktop_and_mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    return width, height


def test_github_main_page_desktop(desktop_and_mobile_browser):
    width, height = desktop_and_mobile_browser
    if width >= 1600:
        browser.open('/')
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip(reason='Skip test because needs desktop size')


def test_github_main_page_mobile(desktop_and_mobile_browser):
    width, height = desktop_and_mobile_browser
    if width < 1600:
        browser.open('/')
        browser.element('[class="flex-1"] [data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in"]'). \
            click()
    else:
        pytest.skip(reason='Skip test because needs mobile size')
