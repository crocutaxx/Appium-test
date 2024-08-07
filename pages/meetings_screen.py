import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class MeetingsScreen(BasePage):

    TODAY_MEETINGS_TEXT = ('xpath', '//android.view.View[@text="Встречи на сегодня"]')
    SCHEDULE_BUTTON = ('xpath', '//android.widget.Button[@content-desc="Запланировать"]')
    STATUS_OF_THE_PLANNING_MEETING = ('xpath', '//android.widget.TextView[@text="Запланирована"]')

    @allure.step("Check authorization")
    def check_authorization(self):
        self.wait.until(EC.visibility_of_element_located(self.TODAY_MEETINGS_TEXT))

    @allure.step("Click on the schedule button")
    def click_on_the_schedule_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SCHEDULE_BUTTON)).click()

    @allure.step("Check status of the planning meeting")
    def check_status_of_the_planning_meeting(self):
        self.wait.until(EC.visibility_of_element_located(self.STATUS_OF_THE_PLANNING_MEETING))


