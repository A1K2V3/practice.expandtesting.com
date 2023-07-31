from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Config.Config import TestData
from Pages.BasePage import BasePage

micro_timeout = 1


class NotificationMessage(BasePage):
    NOTIFICATION_MESSAGE = (By.XPATH, "//div[@id='flash-message']/div[@id='flash']/b[contains(text(),'')]")
    LINK_HERE = (By.LINK_TEXT, "Click here")
    NOTIFICATION_CANCEL_BUTTON = (By.CLASS_NAME, "btn-close")

    def __init__(self, driver) -> None:
        super().__init__(driver)

        self.launch_url(TestData.Notification_Message_Page_Url)

    def click_click_here_link(self, timeout=micro_timeout):
        self.click_on_element(self.LINK_HERE, timeout)

    def verify_notification_exist(self, timeout=micro_timeout):
        return self.is_element_visible(self.NOTIFICATION_MESSAGE, timeout)

    def clear_notification(self, timeout=micro_timeout):
        self.click_on_element(self.NOTIFICATION_CANCEL_BUTTON, timeout)

    def generate_notification(self):
        self.click_click_here_link()
