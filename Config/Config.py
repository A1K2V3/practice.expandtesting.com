from faker import Faker
import random

class TestData:
    WebInputPage_Url = "https://practice.expandtesting.com/inputs"
    WebOutputPage_Number = random.randint(0,100)
    WebOutputPage_Text = Faker().text(max_nb_chars=10)
    WebOutputPage_Password = Faker().password()
    WebOutputPage_Date = Faker().date_between()