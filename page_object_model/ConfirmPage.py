import time

from selenium.webdriver.common.by import By

from BaseDriver.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions

class ConfirmPage(BaseClass):
    def __init__(self, driver, path, wait):
        self.driver = driver
        self.path = path
        self.wait = wait


    input_country = (By.ID, "country")
    #uggestion_list = "//div[@class= 'suggestions']/ul/li/a"
    checkbox = (By.ID, "checkbox2")
    purchase_button = (By.XPATH, "//input[@type = 'submit']")
    order_status = (By.XPATH, "//input[@value = 'Purchase']")

    def select_country(self):
        self.driver.find_element(*ConfirmPage.input_country).send_keys("IND")
        self.wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        time.sleep(2)
        self.driver.find_element(*ConfirmPage.checkbox).click()
        self.driver.find_element(*ConfirmPage.purchase_button)
        final_message = self.driver.find_element(*ConfirmPage.order_status).text
        return final_message






