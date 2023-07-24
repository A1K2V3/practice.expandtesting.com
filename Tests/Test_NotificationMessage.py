import random
import pytest

from Tests.BaseTest import BaseTest

class Test_NotificationMessage(BaseTest):

    def test_succces_notification_message(self, notification_message):
        notification_message.generate_notification()
        assert notification_message.verify_notification_exist()
        notification_message.clear_notification()

    def test_multiple_notification(self, notification_message):
        num = random.randint(0,100)
        for _ in range(num):
            notification_message.generate_notification()
            assert notification_message.verify_notification_exist()

