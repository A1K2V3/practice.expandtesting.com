from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Config.Config import TestData
from Pages.BasePage import BasePage

micro_timeout = 1


class WebInputs(BasePage):
    OUTPUT_NUMBER = (By.ID, "output-number")
    INPUT_NUMBER = (By.ID, "input-number")
    DISPLAY_INPUTS = (By.ID, "btn-display-inputs")
    CLEAR_INPUTS = (By.ID, "btn-clear-inputs")
    OUTPUT_TEXT = (By.ID, "output-text")
    INPUT_TEXT = (By.ID, "input-text")
    OUTPUT_PASSWORD = (By.ID, "output-password")
    INPUT_PASSWORD = (By.ID, "input-password")
    OUTPUT_DATE = (By.ID, "output-date")
    INPUT_DATE = (By.ID, "input-date")

    def __init__(self, driver) -> None:
        """
        The function initializes a class instance with a driver and sets the launch URL to a specific
        web page.

        :param driver: The "driver" parameter is an instance of a web driver, such as Selenium
        WebDriver, that is used to interact with a web browser. It is typically passed to the
        constructor of a page object class to enable the page object to perform actions on the web page
        using the driver
        """
        super().__init__(driver)
        self.launch_url(TestData.WebInputPage_Url)

    def input_number(self, number, timeout=micro_timeout):
        """
        The function `input_number` is used to enter a number into an input field.

        :param number: The number parameter is the value that you want to input into the input field. It
        can be any numerical value that you want to enter
        :param timeout: The `timeout` parameter is the maximum amount of time to wait for the element to
        be interactable before raising a timeout exception. It is an optional parameter and if not
        provided, it will default to a predefined value called `micro_timeout`
        """
        self.enter_text_on_element(self.INPUT_NUMBER, number, timeout)

    def display_inputs(self, timeout=micro_timeout):
        """
        The function "display_inputs" clicks on an element to display inputs.

        :param timeout: The `timeout` parameter is the maximum amount of time to wait for the element to
        be clickable before raising a timeout exception. It is set to a default value of
        `micro_timeout`, which is likely a predefined constant or variable in the code
        """
        self.click_on_element(self.DISPLAY_INPUTS, timeout)

    def clear_inputs(self, timeout=micro_timeout):
        """
        The function clears all input fields on a webpage.

        :param timeout: The timeout parameter is the maximum amount of time to wait for the element to
        be clickable before raising a TimeoutException. It is optional and has a default value of
        micro_timeout
        """
        self.click_on_element(self.CLEAR_INPUTS, timeout)

    def get_output_number(self, timeout=micro_timeout):
        """
        The function `get_output_number` returns the integer value of the text in the element
        `OUTPUT_NUMBER`, or 0 if the element is empty.

        :param timeout: The `timeout` parameter is the maximum amount of time to wait for the element to
        be visible and have text before raising a timeout exception. It is set to a default value of
        `micro_timeout`, which is likely a predefined constant representing a very short duration of
        time
        :return: an integer value. If the `number` variable is not empty, it will be converted to an
        integer using the `int()` function and returned. If the `number` variable is empty, the function
        will return 0.
        """
        number = self.get_element_text(self.OUTPUT_NUMBER, timeout)
        return int(number) if number else 0

    def input_number_by_mouse_click(self, number, timeout=micro_timeout):
        """
        The function takes a number as input and calculates the difference between that number and the
        current value in an input field, then determines whether to click the arrow up or arrow down key
        based on the difference.

        :param number: The number parameter represents the desired number that you want to input using
        mouse clicks
        :param timeout: The `timeout` parameter is the maximum amount of time to wait for the element to
        be visible and clickable before raising a timeout exception. It is set to a default value of
        `micro_timeout`, which is likely a predefined constant representing a very short duration of
        time
        """
        output_nubmer = self.get_element_text(self.INPUT_NUMBER, timeout) or 0
        clicks = number - int(output_nubmer)
        key = Keys.ARROW_DOWN if clicks < 0 else Keys.ARROW_UP

        self.click_on_element(self.INPUT_NUMBER, timeout)
        for _ in range(abs(clicks)):
            self.press_key(key)

    def input_text(self, text, timeout=micro_timeout):
        """
        The function `input_text` is used to enter text into an input field.

        :param text: The `text` parameter is the string of text that you want to input into the text
        field
        :param timeout: The timeout parameter is the maximum amount of time to wait for the input
        element to be visible and enabled before throwing an exception. It is optional and defaults to a
        predefined micro_timeout value
        """
        self.enter_text_on_element(self.INPUT_TEXT, text, timeout)

    def get_output_text(self, timeout=micro_timeout):
        """
        The function returns the text of an output element.

        :param timeout: The timeout parameter is the maximum amount of time to wait for the output text
        to be available before raising a timeout exception. It is set to a default value of
        micro_timeout, which is likely a very short duration
        :return: The method is returning the element text of the OUTPUT_TEXT element.
        """
        return self.get_element_text(self.OUTPUT_TEXT, timeout)

    def input_password(self, passowrd, timeout=micro_timeout):
        """
        The function `input_password` is used to enter a password into an input field.

        :param passowrd: The parameter "passowrd" is likely a typo and should be corrected to
        "password". It represents the password that will be entered into the input field
        :param timeout: The `timeout` parameter is the maximum amount of time to wait for the element to
        be visible and interactable before raising a timeout exception. It is an optional parameter with
        a default value of `micro_timeout`
        """
        self.enter_text_on_element(self.INPUT_PASSWORD, passowrd, timeout)

    def get_output_password(self, timeout=micro_timeout):
        """
        The function returns the text of the output password element.

        :param timeout: The timeout parameter is the maximum amount of time to wait for the element to
        be visible and have text before raising a TimeoutException. It is measured in seconds. The
        default value is micro_timeout, which is a small value typically used for quick operations
        :return: the element text of the OUTPUT_PASSWORD element.
        """
        return self.get_element_text(self.OUTPUT_PASSWORD, timeout)

    def input_date(self, date, timeout=micro_timeout):
        """
        The function takes a date input, formats it, and then enters it into an input field.

        :param date: The `date` parameter is the date that you want to input. It should be a
        `datetime.date` object representing the date you want to input
        :param timeout: The `timeout` parameter is the maximum amount of time to wait for an element to
        be interactable before raising a timeout exception. It is set to a default value of
        `micro_timeout`, which is likely a predefined constant representing a very short duration of
        time
        """
        # self.enter_text_on_element(self.INPUT_DATE, str(date), timeout)
        date = "".join(str(date.strftime("%d/%m/%Y")).split("/"))
        self.click_on_element(self.INPUT_DATE, timeout)
        for num in date:
            key = getattr(Keys, f"NUMPAD{num}")
            self.press_key(key)

    def get_output_date(self, timeout=micro_timeout):
        """
        The function returns the text of the output date element.

        :param timeout: The timeout parameter is the maximum amount of time to wait for the element to
        be visible and have text before raising a TimeoutException. It is optional and defaults to a
        micro_timeout value
        :return: the output date.
        """
        return self.get_element_text(self.OUTPUT_DATE, timeout)
