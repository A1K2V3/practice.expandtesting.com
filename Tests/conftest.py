import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.firefox.service import Service as firefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Pages.WebInputs import WebInputs
from Pages.AddRemoveElements import AddRemoveElements
from Pages.NotificationMessage import NotificationMessage


# @pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    """
    The above function is a pytest fixture that initializes a web driver based on the parameter passed
    and assigns it to the class attribute "driver".

    :param request: The `request` parameter is a special fixture provided by pytest. It represents the
    current test request and provides access to various information and functionalities related to the
    test being executed. In this case, it is used to access the test parameter (`request.param`) and set
    up the appropriate web driver based on the
    """
    if request.param == "chrome":
        options = chromeOptions()
        driver = webdriver.Chrome(service=chromeService(
            ChromeDriverManager().install()), options=options)

    elif request.param == "firefox":
        options = firefoxOptions()
        driver = webdriver.Firefox(service=firefoxService(
            GeckoDriverManager().install()), options=options)

    elif request.param == "edge":
        options = edgeOptions()
        driver = webdriver.Edge(service=edgeService(
            EdgeChromiumDriverManager().install()), options=options)

    driver.maximize_window()
    driver.delete_all_cookies()
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture
def webinput(request):
    """
  The function `webinput` is a pytest fixture that returns an instance of the `WebInputs` class,
  initialized with the `driver` attribute from the `request.cls` object.

  :param request: The `request` parameter is an object that provides information about the currently
  running test. It is provided by the pytest framework and can be used to access various attributes
  and methods related to the test execution
  :return: The fixture is returning an instance of the WebInputs class, which is initialized with the
  driver object.
  """
    return WebInputs(request.cls.driver)

@pytest.fixture
def add_remove_element(request):
    return AddRemoveElements(request.cls.driver)

@pytest.fixture
def notification_message(request):
    return NotificationMessage(request.cls.driver)
