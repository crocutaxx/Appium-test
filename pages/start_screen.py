import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class StartScreen(BasePage):

    CONNECT_TO_MEETING_BY_ID = ('xpath', '//android.widget.Button[@content-desc="Подключиться к встрече"]')
    SIGN_IN_BUTTON = ('xpath', '//android.widget.TextView[@text="Вход"]')

    @allure.step("Click on connect to meeting button")
    def click_on_connect_to_meeting_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CONNECT_TO_MEETING_BY_ID)).click()

    @allure.step("Click on sign in button")
    def click_on_sign_in_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SIGN_IN_BUTTON)).click()
