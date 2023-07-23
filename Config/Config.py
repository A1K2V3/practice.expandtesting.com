from faker import Faker
import random

class TestData:

    #################### WebInputPage#########################################################
    WebInputPage_Url = "https://practice.expandtesting.com/inputs"
    
    WebOutputPage_Number = random.randint(0,100)
    WebOutputPage_Text = Faker().text(max_nb_chars=10)
    WebOutputPage_Password = Faker().password()
    WebOutputPage_Date = Faker().date_between()

    ########################### for paramertised run on webInput Page #########################
    web_input_numbers = [random.randint(1, 10**10) for _ in  range(100)]
    web_input_text = [Faker().text(max_nb_chars=random.randint(5, 100)) for _ in range(100)]
    web_input_password = [Faker().password(length=random.randint(10, 40)) for _ in range(100)]
    web_input_date = [Faker().date_between(start_date='-2022y', end_date='+7976y') for _ in range(100)]
    
