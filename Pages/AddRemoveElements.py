import random
from selenium.webdriver.common.by import By
from Config.Config import TestData
from Pages.BasePage import BasePage

micro_timeout = 1


class AddRemoveElements(BasePage):
    ADD_ELEMENT = (By.XPATH, "//*[@class='btn btn-primary mt-3']")
    DELETE_BUTTON = (By.XPATH, "//*[@id='elements']/button")

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.launch_url(TestData.AddRemoveElementsPage_Url)

    def get_add_remove_page_title(self):
        return self.get_page_title()

    def add_element(self, no_of_elements, timeout=micro_timeout):
        for _ in range(no_of_elements):
            print("adding element")
            self.click_on_element(self.ADD_ELEMENT, timeout)

    def delete_element(self, element_index, timeout=micro_timeout):
        locator = f"({self.DELETE_BUTTON[1]})[{element_index + 1}]"
        print("locator")
        print(locator)
        self.click_on_element((self.DELETE_BUTTON[0], locator), timeout)

    def delete_elements(self, number, timeout=micro_timeout):
        while number:
            self.delete_element(random.randint(0, number - 1), timeout)
            number -= 1

    def count_delete_buttons(self):
        return len(self.find_all_elements(self.DELETE_BUTTON))
