import pytest
from selenium.webdriver.support import expected_conditions
from Utilities import *

@pytest.mark.usefixtures("setup")
class BaseClass:
    path = r'C:\Users\prasa\OneDrive\Desktop\pythonProject\udemy_course_project\Data\Data_set.xlsx'

    def verify_link_presence(self, locator_type, locator):
        return self.wait.until(expected_conditions.presence_of_element_located((locator_type, locator)))