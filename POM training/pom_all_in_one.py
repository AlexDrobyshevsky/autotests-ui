# import pytest
# from playwright.sync_api import Page, expect
#
#
# class BasePage:
#     def __init__(self, page: Page):
#         self.page = page
#
#     def visit(self, url: str):
#         self.page.goto(url, wait_until='networkidle')
#
#
# class RegistrationPage(BasePage):
#     def __init__(self, page: Page):
#         super().__init__(page)
#
#         self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#         self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#         self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#         self.registration_button = page.get_by_test_id('registration-page-registration-button')
#
#     def fill_registration_form(self, email: str, username: str, password: str):
#         self.email_input.fill(email)
#         self.username_input.fill(username)
#         self.password_input.fill(password)
#
#     def click_registration_button(self):
#         self.registration_button.click()
#
#
# class DashboardPage(BasePage):
#     def __init__(self, page: Page):
#         super().__init__(page)
#
#         self.dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
#
#     def check_dashboard_title(self):
#         expect(self.dashboard_title).to_be_visible()
#         expect(self.dashboard_title).to_have_text('Dashboard')
#
#
# @pytest.fixture
# def registration_page(chromium_page: Page):
#     return RegistrationPage(page=chromium_page)
#
#
# @pytest.fixture
# def dashboard_page(chromium_page: Page):
#     return DashboardPage(page=chromium_page)
#
#
# # @pytest.mark.regression
# # @pytest.mark.registration
# def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
#     registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
#     registration_page.fill_registration_form(email='user.name@gmail.com', username='username', password='password')
#     registration_page.click_registration_button()
#
#     dashboard_page.check_dashboard_title()

class Brand:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self):
        self.brand = None

    def set_brand(self, brand):
        self.brand = brand


bmw = Brand("BMW")

car = Car()
car.set_brand(bmw)

print(car.brand)

print(car.brand.name)
