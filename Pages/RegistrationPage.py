import random
import string
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class RegistrationPage(BasePage):

    ENTER_LINK    = (By.XPATH, '//span/a[@class="enter_link"]')
    REGISTRATION  = (By.CLASS_NAME, 'registration')
    FIRST_NAME    = (By.NAME, 'firstname')
    LAST_NAME     = (By.NAME, 'lastname')
    BIRTH         = (By.NAME, 'dob')
    SAVE_BIRTH    = (By.XPATH, '//button[contains(@class, "applyBtn")]')
    EMAIL         = (By.NAME, 'email_address')
    PHONE_NUMBER  = (By.NAME, 'telephone')
    CITY          = (By.NAME, 'city')
    REGION        = (By.XPATH, '//input[@placeholder="Область:"]')
    POST_CODE     = (By.NAME, 'postcode')
    PASSWORD      = (By.NAME, 'password')
    CONF_PASSWORD = (By.NAME, 'confirmation')
    SUBMIT        = (By.XPATH, '//input[@type="submit"]')
    SHOP_RULES    = (By.XPATH, '//input[@name="shoprules"]/following::label')
    SUCCESS       = (By.XPATH, '//center[text()="Ваш аккаунт успішно створений!"]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_registration_form(self):
        self.do_click(self.ENTER_LINK)
        self.do_click(self.REGISTRATION)

    def send_all_fields(self, first_name, last_name, birth, email, phone, city, region, post_code, password,
                        shop_rule=True):
        self.do_send_keys(self.FIRST_NAME, first_name)
        self.do_send_keys(self.LAST_NAME, last_name)
        self.do_send_keys(self.BIRTH, birth)
        self.do_click(self.SAVE_BIRTH)
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PHONE_NUMBER, phone)
        self.do_send_keys(self.CITY, city)
        self.choose_drop_down_item(self.REGION, (By.XPATH, f'//div[text()="{region}"]'))
        self.do_send_keys(self.POST_CODE, post_code)
        self.do_send_keys(self.PASSWORD, password)
        self.do_send_keys(self.CONF_PASSWORD, password)
        shop_rule and self.do_click(self.SHOP_RULES)

    @staticmethod
    def get_random_string(length):
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def get_random_number(length):
        digits = string.digits
        return ''.join(random.choice(digits) for _ in range(length))
