from elements.link import Link
from pages.base_page import BasePage
from playwright.sync_api import Page
from components.authentication.registration_form_component import RegistrationFormComponent


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_form = RegistrationFormComponent(page)

        self.login_link = Link(page, 'registration-page-login-link', 'Login')

    def click_login_link(self):
        self.login_link.click()
