import pytest

from BaseDriver.BaseClass import BaseClass
from page_object_model.ConfirmPage import ConfirmPage
from page_object_model.home_page import HomePage
from page_object_model.shop_page import ShopPage


class TestOne(BaseClass):
    def test_invoke_url(self):
        title = self.driver.title
        assert 'ProtoCommerce' in title
        print("Browser Opened successfully")

    def test_fill_form(self):
        hp = HomePage(self.driver, self.path)
        assert "Success" in hp.fill_details()
        print("Form filled succesfully")


    def test_add_to_cart(self):
        sp = ShopPage(self.driver, self.path)
        sp.select_product()

    def test_final_order(self):
        cp = ConfirmPage(self.driver, self.path, self.wait)
        assert "Success! Thank You!" in cp.select_country()

