import pytest
import time
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# Here are texts from button "Add to basket" from different localizing.
# You can make sure, that test works if choose Danish (language = da). I didn't add this text.
# This way test will fall.


class TestItems(object):
    """
    This class checks if the guest sees the "Add to cart" button.
    """

    def test_if_cart_btn_available(self, browser):
        browser.get(link)
        button = browser.find_element_by_css_selector("button.btn-add-to-basket")
        assert button.is_enabled, 'Button "Add to cart" not found.'
