from Pages.RegistrationPage import RegistrationPage
from Tests.test_base import BaseTest


class TestsRegistration(BaseTest):

    @classmethod
    def setup_method(cls):
        cls.registration_page = RegistrationPage(cls.driver)

    def test_registrate(self):
        self.registration_page.get_page()
        self.registration_page.open_registration_form()
        letters = self.registration_page.get_random_string(7)
        numbers = self.registration_page.get_random_number(6)
        self.registration_page.send_all_fields(first_name=letters, last_name=letters, birth='03/02/1999',
                                               email=f'{letters}@gmail.com', phone=f'+380{numbers}',
                                               city='Kyiv', region='Николаевская область', post_code=numbers,
                                               password=letters+numbers)
        self.registration_page.do_click(self.registration_page.SUBMIT)
        assert self.registration_page.is_visible(self.registration_page.SUCCESS)
