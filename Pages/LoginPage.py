from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):

    ENTER_LINK   = (By.XPATH, '//span/a[@class="enter_link"]')
    EMAIL        = (By.NAME, 'email_address')
    PASSWORD     = (By.NAME, 'password')
    SUBMIT       = (By.NAME, 'submit_enter')
    ENTER_WINDOW = (By.CLASS_NAME, 'client-enter_window')
    ACC_HISTORY  = (By.XPATH, '//span/a[@href="account_history.php"]')

    def __init__(self, driver):
        super().__init__(driver)

    def open_modal(self):
        self.do_click(self.ENTER_LINK)
        return self.is_visible(self.ENTER_WINDOW)

    def do_login(self, email, password):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.SUBMIT)

    def open_acc_history(self):
        self.do_click(self.ACC_HISTORY)
