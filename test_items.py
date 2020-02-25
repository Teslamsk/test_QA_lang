import pytest
import time
from selenium import webdriver

# В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления +
# в корзину. Например, можно проверять товар, доступный +
# по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/. +

# Ваше решение будет проверяться по следующим критериям:
#
# Тест в репозитории можно запустить командой pytest --language=es, тест успешно проходит. +
# Проверка работоспособности кода для разных языков. Добавьте в файл с тестом команду time.sleep(30) сразу после +
# открытия ссылки. Запустите тест с параметром --language=fr и визуально проверьте, что фраза на кнопке добавления в корзину выглядит так: "Ajouter au panier". +
# Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр. +
# В тесте проверяется наличие кнопки добавления в корзину. Селектор кнопки является уникальным для
# проверяемой страницы. + Есть assert. +
# Название тестового метода внутри файла test_items.py соответствует задаче. +
# Название test_something не удовлетворяет требованиям. +


# Убедиться в том, что тест успешно проваливается - можно если ввести парметр датского языка 'da'

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

right_answers = ("Добавить в корзину",
                 "Add to basket",
                 "Añadir al carrito",
                 "Ajouter au panier",
                 "In Warenkorb legen",
                 "Aggiungi al carrello",
                 "أضف الى سلة التسوق",
                 "Додати в кошик",
                 "장바구니 담기",
                 )


class TestItems(object):
    """
    This class checks if the guest sees the "Add to cart" button.
    """

    def test_item(self, browser):
        browser.get(link)
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        assert button.text in right_answers
        time.sleep(5)
