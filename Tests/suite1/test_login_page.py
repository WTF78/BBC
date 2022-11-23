from Pages.LoginPage import LoginPage
from Tests.config import TestData
from Tests.test_base import BaseTest


class TestsLogin(BaseTest):

    @classmethod
    def setup_method(cls):
        cls.login_page = LoginPage(cls.driver)

    def test_login(self):
        self.login_page.get_page()
        self.login_page.open_modal()
        self.login_page.do_login(TestData.EMAIL, TestData.PASSWORD)
        self.login_page.open_acc_history()
