import os
import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class SignInScreen(BasePage):

    EMAIL_FIELD = ('xpath', '//android.widget.EditText[@text="Email"]')
    PASSWORD_FIELD = ('xpath', '//android.widget.EditText[@text="Пароль"]')
    ENTER_BUTTON = ('xpath', '//android.widget.TextView[@text="Вход"]')

    @allure.step("Enter email address")
    def enter_email_address(self):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD)).send_keys(os.getenv("LOGIN2"))

    @allure.step("Enter password")
    def enter_password(self):
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD)).send_keys(os.getenv("PASSWORD2"))

    @allure.step("Click on the Enter button")
    def click_on_enter_button(self):
        self.wait.until(EC.visibility_of_element_located(self.ENTER_BUTTON)).click()
