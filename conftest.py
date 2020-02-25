import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Parametrize browser for tests
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    # Parametrize language for site
    parser.addoption('--user_language', action='store', default='ru', help="Choose language: ru or en-gb")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("user_language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
    else:
        raise pytest.UsageError(f"--your browser {browser_name} with language {user_language} still not implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()


# В конструктор webdriver.Chrome или webdriver.Firefox вы можете добавлять разные аргументы, расширяя возможности
# тестирования ваших веб-приложений: можно указывать прокси-сервер для контроля сетевого трафика или запускать разные
# версии браузера, указывая локальный путь к файлу браузера. Предполагаем, что эти возможности вам понадобятся позже
# и вы сами сможете найти настройки для этих задач.
