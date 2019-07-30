import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', \
                     action='store', \
                     default="chrome", \
                     help="Choose browser ('chrome' is default)")
    parser.addoption('--language', \
                     action='store', \
                     default='en', \
                     help="Choose language ('en' is default)")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', \
                                        {'intl.accept_languages': user_language})
        print("\n\nStart Chrome browser for test...")
        browser = webdriver.Chrome(options=options)
    elif (browser_name == "firefox"):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\n\nStart Firefox browser for test...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else: 
        print("Browser <browser_name> still is not implemented")
    yield browser
    print("\nQuit browser...")
    browser.quit() 
