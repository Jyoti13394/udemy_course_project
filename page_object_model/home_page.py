from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from BaseDriver.BaseClass import BaseClass
from Utilities import *


class HomePage:

    def __init__(self, driver):
        self.driver = driver
    input_name = (By.NAME, "name")
    input_email = (By.XPATH, "//input[@name = 'email']")
    input_password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    employed_radio_button = (By.ID, "inlineRadio2")
    submit_button = (By.XPATH, "//input[@type='submit']")
    form_submit_status_text = (By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']")
    path = r'C:\Users\prasa\OneDrive\Desktop\pythonProject\udemy_course_project\Data\Data_set.xlsx'

    def fill_details(self):
        ut = Utilities
        input_data = ut.data_from_excel_to_dict(HomePage.path)
        self.driver.find_element(*HomePage.input_name).send_keys(input_data['Name'])
        self.driver.find_element(*HomePage.input_email).send_keys(input_data['Email'])
        self.driver.find_element(*HomePage.input_password).send_keys(input_data['Password'])
        select_gender_dropdown = Select(self.driver.find_element(*HomePage.gender))
        select_gender_dropdown.select_by_visible_text(input_data['Gender'])
        self.driver.find_element(*HomePage.employed_radio_button).click()
        self.driver.find_element(*HomePage.submit_button).click()
        submit_message = self.driver.find_element(*HomePage.form_submit_status_text).text



