import pytest

from Config.Config import TestData
from Tests.BaseTest import BaseTest


class Test_WebInput(BaseTest):

    def test_input_number(self, webinput):
        number = TestData.WebOutputPage_Number
        webinput.clear_inputs()
        webinput.input_number(number)
        webinput.display_inputs()
        assert webinput.get_output_number() == number

    def test_input_text(self, webinput):
        text = TestData.WebOutputPage_Text
        webinput.clear_inputs()
        webinput.input_text(text)
        webinput.display_inputs()
        assert webinput.get_output_text() == text

    def test_input_password(self, webinput):
        password = TestData.WebOutputPage_Password
        webinput.clear_inputs()
        webinput.input_password(password)
        webinput.display_inputs()
        assert webinput.get_output_password() == password

    def test_input_date(self, webinput):
        date = TestData.WebOutputPage_Date
        webinput.clear_inputs()
        webinput.input_date(date)
        webinput.display_inputs()
        assert webinput.get_output_date() == str(date)

    def test_input_number_by_mouse_click(self, webinput):
        number = TestData.WebOutputPage_Number
        webinput.clear_inputs()
        webinput.input_number_by_mouse_click(number)
        webinput.display_inputs()
        assert webinput.get_output_number(number) == number
