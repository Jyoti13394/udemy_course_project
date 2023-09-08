from selenium.webdriver.common.by import By
from Utilities import *


class ShopPage:
    def __init__(self, driver, path):
        self.driver = driver
        self.path = path

    product_list = (By.XPATH, "//div[@class='card h-100']")
    checkout_button = (By.XPATH, "//a[@class= 'nav-link btn btn-primary']")
    proceed_button = (By.XPATH, "//button[@class = 'btn btn-success']")

    def select_product(self):
        ut = Utilities
        input_data = ut.data_from_excel_to_dict(self.path)
        list_of_product = self.driver.find_elements(*ShopPage.product_list)
        for product in list_of_product:
            if product.find_element(By.XPATH, "div/h4/a").text == input_data['Product']:
                product.find_element(By.XPATH, "div[2]/button[@class = 'btn btn-info']").click()

        self.driver.find_element(*ShopPage.checkout_button).click()
        assert input_data['Product'] in self.driver.find_element(By.XPATH, "//a[text() = 'Blackberry']").text
        print("Required Product Added Succesfully")
        self.driver.find_element(*ShopPage.proceed_button).click()
        print("Proceeded to Final Order Page")


