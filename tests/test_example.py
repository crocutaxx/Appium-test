import allure
from base.base_test import BaseTest
import pytest


@allure.feature("Authorization functionality")
class TestStart(BaseTest):

    @allure.title("Valid authorization")
    def test_authorization(self):

        self.start_screen.click_on_sign_in_button()
        self.sign_in_screen.enter_email_address()
        self.sign_in_screen.enter_password()
        self.sign_in_screen.click_on_enter_button()
        self.meetings_screen.check_authorization()

    @pytest.mark.regression
    @allure.title("Schedule an meeting")
    def test_schedule_meeting(self, auth_user, user_1):

        self.meetings_screen.check_authorization()
        self.meetings_screen.click_on_the_schedule_button()
        self.schedule_screen.enter_topic_name()
        self.schedule_screen.click_on_schedule_meeting_button()
        self.meetings_screen.check_status_of_the_planning_meeting()

