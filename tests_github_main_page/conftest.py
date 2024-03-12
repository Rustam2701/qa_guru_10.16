import pytest
from selene import browser


@pytest.fixture(params=['desktop', 'mobile'], scope='session', autouse=True)
def browser_manager_desktop(request):
    if request.param == 'desktop':
        browser.config.base_url = 'https://github.com/'
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'mobile':
        browser.config.base_url = 'https://github.com/'
        browser.config.window_width = 414
        browser.config.window_height = 896

    yield

    browser.quit()
