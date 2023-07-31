import pytest
import random
from Tests.BaseTest import BaseTest
from Config.Config import TestData


class Test_AddRemoveElements(BaseTest):

    def test_verify_title(self, add_remove_element):
        assert add_remove_element.get_add_remove_page_title() == TestData.AddRemoveElementsPage_Title

    def test_add_delete_element(self, add_remove_element, number=random.randint(0, 100)):
        add_remove_element.add_element(number)
        add_remove_element.delete_elements(number)
        assert add_remove_element.count_delete_buttons() == 0
