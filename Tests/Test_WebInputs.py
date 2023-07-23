import pytest

from Config.Config import TestData
from Tests.BaseTest import BaseTest


class Test_WebInput(BaseTest):

    def test_verify_title(self, webinput):
        assert webinput.get_webinput_page_title() == "Web inputs"

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
        assert webinput.get_output_date() == date

    def test_input_number_by_mouse_click(self, webinput):
        number = TestData.WebOutputPage_Number
        webinput.clear_inputs()
        webinput.input_number_by_mouse_click(number)
        webinput.display_inputs()
        assert webinput.get_output_number(number) == number

    @pytest.mark.parametrize("number, text, password, date", zip(TestData.web_input_numbers, TestData.web_input_text, TestData.web_input_password, TestData.web_input_date))
    def test_all_inputs(self, webinput, number, text, password, date):
        webinput.clear_inputs()
        webinput.input_number(number)
        webinput.input_text(text)
        webinput.input_password(password)
        webinput.input_date(date)
        webinput.display_inputs()
        assert webinput.get_output_number() == number
        assert webinput.get_output_text() == text
        assert webinput.get_output_password() == password
        assert webinput.get_output_date() == date