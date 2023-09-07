import pytest

from BaseDriver.BaseClass import BaseClass
from page_object_model.home_page import HomePage


class TestOne(BaseClass):
    def test_invoke_url(self):
        title = self.driver.title
        assert 'ProtoCommerce' in title
        print("Browser Opened successfully")

    def test_fill_form(self):
        hp = HomePage(self.driver)
        hp.fill_details()
