import pytest
from pages.start_screen import StartScreen
from pages.sign_in_screen import SignInScreen
from pages.meetings_screen import MeetingsScreen
from pages.schedule_screen import ScheduleScreen

class BaseTest:

    start_screen: StartScreen
    sign_in_screen: SignInScreen
    meetings_screen: MeetingsScreen
    schedule_screen: ScheduleScreen

    @pytest.fixture(scope="function")
    def user_1(self, request, driver):
        request.cls.driver = driver

        request.cls.start_screen = StartScreen(driver)
        request.cls.sign_in_screen = SignInScreen(driver)
        request.cls.meetings_screen = MeetingsScreen(driver)
        request.cls.schedule_screen = ScheduleScreen(driver)
