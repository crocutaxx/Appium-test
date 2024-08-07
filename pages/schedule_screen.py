import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ScheduleScreen(BasePage):

    TOPIC_NAME_FIELD = ('xpath', '//android.widget.EditText[@text="Тема"]')
    SCHEDULE_MEETING_BUTTON = ('xpath', '//android.widget.Button[@content-desc="Запланировать встречу"]')

    @allure.step("Enter topic name")
    def enter_topic_name(self):
        self.wait.until(EC.visibility_of_element_located(self.TOPIC_NAME_FIELD)).send_keys('TestMeeting')

    @allure.step("Click on schedule meeting button")
    def click_on_schedule_meeting_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SCHEDULE_MEETING_BUTTON)).click()


