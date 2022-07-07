import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language:es")

@pytest.fixture()
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language == "es":
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages':
        'es'})
        browser = webdriver.Chrome(options=options) 
    else: 
        print("\nstart browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages':
        'fr'})  #пока недопоняла: нужен список всех доступных языков для сайта? 
        browser = webdriver.Chrome(options=options)
            
    yield browser
    print("\nquit browser..")
    browser.quit()