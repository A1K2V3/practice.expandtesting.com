from faker import Faker
import random

class TestData:

    #################### WebInputPage#########################################################
    WebInputPage_Url = "https://practice.expandtesting.com/inputs"
    WebInputPage_Title = "Web inputs"   
    
    WebOutputPage_Number = random.randint(0,100)
    WebOutputPage_Text = Faker().text(max_nb_chars=10)
    WebOutputPage_Password = Faker().password()
    WebOutputPage_Date = Faker().date_between()

    ########################### for paramertised run on webInput Page #########################
    web_input_numbers = [random.randint(1, 10**10) for _ in  range(100)]
    web_input_text = [Faker().text(max_nb_chars=random.randint(5, 100)) for _ in range(100)]
    web_input_password = [Faker().password(length=random.randint(10, 40)) for _ in range(100)]
    web_input_date = [Faker().date_between(start_date='-2022y', end_date='+7976y') for _ in range(100)]


    ####################################### Add Remove Element Page###########################
    AddRemoveElementsPage_Url = "https://practice.expandtesting.com/add-remove-elements"
    AddRemoveElementsPage_Title = "Test Automation Practice: Working with web Elements (Add and Remove)"

    #################################### Notification Message ################################
    Notification_Message_Page_Url = "https://practice.expandtesting.com/notification-message-rendered"
    Success_Notification = "Action successful"
    Failed_Notification = "Action unsuccessful, please try again"
    
