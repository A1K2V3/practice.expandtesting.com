import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver


class BasePage:

    def __init__(self, driver) -> None:
        """
        The above function is a constructor that initializes an instance of a class with a driver
        object.

        :param driver: The "driver" parameter is typically used in the context of web automation or
        testing frameworks such as Selenium. It represents the web browser or the driver instance that
        will be used to interact with the web page
        """
        self.driver = driver

        # self.driver = webdriver.Chrome()
        self.action = ActionChains(self.driver)

    def launch_url(self, url):
        """
        The function launches a specified URL in a web browser.

        :param url: The `url` parameter is a string that represents the URL of the webpage you want to
        navigate to
        """
        self.driver.get(url)

    def get_page_title(self):
        """
        The function returns the title of the current web page.
        :return: The title of the current web page.
        """
        return self.driver.title

    def get_page_source(self):
        """
        The function returns the page source of a web page.
        :return: The method `get_page_source` is returning the page source of the web page being
        accessed by the `self.driver` object.
        """
        return self.driver.page_source

    def quit(self):
        """
        The above function is used to quit the driver in a Python script.
        """
        self.driver.quit()

    def wait_for_page_to_load(self, timout):
        """
        The function waits for a web page to finish loading within a specified timeout period.

        :param timout: The `timout` parameter is the maximum amount of time (in seconds) that the
        function will wait for the page to load before returning False
        :return: The method is returning the `self.driver` object if the page finishes loading within
        the specified timeout. If the page does not finish loading within the timeout, it returns
        `False`.
        """
        counter = 0
        while counter < timout:
            time.sleep(1)
            counter += 1
            if self.driver.execute_script("return document.readyState") in ("complete", "interactive"):
                return self.driver
        else:
            return False

    def click_on_element(self, by_locator, timeout):
        """
        The function waits for an element to be visible and then clicks on it.

        :param by_locator: The by_locator parameter is used to locate the element on the web page. It
        can be specified using various methods provided by the Selenium WebDriver, such as By.ID,
        By.XPATH, By.CSS_SELECTOR, etc. This parameter helps in identifying the element that needs to be
        clicked
        :param timeout: The timeout parameter is the maximum amount of time to wait for the element to
        be visible before throwing a TimeoutException. It is specified in seconds
        """
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(by_locator)).click()

    def enter_text_on_element(self, by_locator, text, timeout):
        """
        The function enters text on a web element identified by a locator after waiting for it to become
        visible.

        :param by_locator: The by_locator parameter is used to locate the element on the web page. It
        can be specified using various methods provided by the Selenium WebDriver, such as By.ID,
        By.XPATH, By.CSS_SELECTOR, etc
        :param text: The "text" parameter is the text that you want to enter into the element
        :param timeout: The timeout parameter is the maximum amount of time to wait for the element to
        be visible before throwing a TimeoutException. It is specified in seconds
        """
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator, timeout):
        """
        The function `get_element_text` returns the text of a web element located by a given locator,
        after waiting for it to become visible within a specified timeout.

        :param by_locator: The by_locator parameter is used to locate the element on the web page. It
        can be an instance of a By class from the selenium.webdriver.common.by module, such as By.ID,
        By.XPATH, By.CSS_SELECTOR, etc. It specifies the method to locate the element
        :param timeout: The timeout parameter is the maximum amount of time to wait for the element to
        become visible before throwing a TimeoutException. It is specified in seconds
        :return: The method is returning the text of the element located by the given locator.
        """
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)).text

    def is_element_visible(self, by_locator, timeout):
        """
        The function checks if an element is visible on a web page within a specified timeout period.

        :param by_locator: The by_locator parameter is used to locate the element on the web page. It
        can be an instance of a By class, such as By.ID, By.XPATH, By.CSS_SELECTOR, etc. It specifies
        the method to locate the element
        :param timeout: The timeout parameter is the maximum amount of time to wait for the element to
        become visible. It is specified in seconds
        :return: a boolean value indicating whether the element located by the given locator is visible
        or not.
        """
        return bool(WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(by_locator)))

    def press_key_on_element(self, by_locator, key, timeout):
        """
        The function `press_key_on_element` sends a key press event to a web element identified by a
        locator, with a specified timeout.
        
        :param by_locator: The by_locator parameter is used to locate the element on the webpage. It can
        be a tuple containing the locator strategy (e.g., By.ID, By.XPATH, etc.) and the locator value
        (e.g., "id_value", "xpath_value", etc.)
        :param key: The "key" parameter in the "press_key_on_element" function is the key or keys that
        you want to send to the element. It can be a single key or a combination of keys. For example,
        if you want to send the "Enter" key, you can pass the value "
        :param timeout: The timeout parameter is the maximum amount of time (in seconds) that the
        function will wait for the element to become visible before giving up and returning False
        :return: a boolean value. If the element is visible and the key is successfully pressed, it
        returns True. If the element is not visible or the key is not pressed within the specified
        timeout, it returns False.
        """
        counter = 0
        while counter < timeout:
            if self.is_elemen_visible:
                self.driver.find_element(by_locator).send_keys(key)
            return True
        else:
            return False

    def press_key(self, key):
        """
        The function "press_key" sends a key press action to the specified element.
        
        :param key: The "key" parameter in the "press_key" method is the key that you want to press on
        the keyboard. It can be any valid key on the keyboard, such as letters, numbers, special
        characters, or function keys
        """
        self.action.send_keys(key)
        self.action.perform()

    def find_all_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def reload_page(self):
        self.driver.refresh()
