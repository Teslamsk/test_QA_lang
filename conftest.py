import pytest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options

# Дорогой друг. Пишу по-русски, потому что ты можешь не знать английского (ну мало ли, китайский учил?).
# Обрати внимание, что у меня в конструкторе браузера для FireFox прописан путь до ланчера.
# Сделано это так потому, что по-другому не работает. Если решишь запустить браузер еще и в FireFox -
# сначала укажи правильный путь к ланчеру. Остальные комментарии на английском, потому что так надо.

# Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
# Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
# Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
# Тест должен запускаться с параметром language следующей командой:
# pytest --language=es test_items.py
# и проходить успешно. Достаточно, чтобы код работал только для браузера Сhrome.

def pytest_addoption(parser):
    # Parameterization of the test by browser
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    # Parameterization of the test by language
    parser.addoption('--language', action='store', default='ru', help="Choose language: ru, en, es, fr etc.")


@pytest.fixture(scope="function")
def browser(request):
    # Enter the browser_name parameter in the browser constructor
    browser_name = request.config.getoption("browser_name")
    # Enter the language parameter in the browser constructor
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        # Setup language parameter for Chrome
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart chrome browser for test..")
        # Launch Chrome
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        # Setup language parameter for FireFox
        binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        print("\nstart firefox browser for test..")
        # Launch FireFox
        browser = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp)
    else:
        raise pytest.UsageError(f"--your browser {browser_name} with language {language} still not implemented")
    yield browser
    print("\nquit browser..")
    browser.quit()


# В конструктор webdriver.Chrome или webdriver.Firefox вы можете добавлять разные аргументы, расширяя возможности
# тестирования ваших веб-приложений: можно указывать прокси-сервер для контроля сетевого трафика или запускать разные
# версии браузера, указывая локальный путь к файлу браузера. Предполагаем, что эти возможности вам понадобятся позже
# и вы сами сможете найти настройки для этих задач.
