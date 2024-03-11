from selene import browser

def test_guthub_main_paig():
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
