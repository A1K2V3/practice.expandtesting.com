import pytest

# The `@pytest.mark.usefixtures("init_driver")` decorator is used to specify that the `init_driver`
# fixture should be used for the test class `BaseTest`.
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass