from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    login_password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    login_button = chromium_page.get_by_test_id('login-page-login-button')

    expect(login_email_input).to_be_visible()
    expect(login_password_input).to_be_visible()
    expect(login_button).to_be_visible()

    registration_link = chromium_page.get_by_test_id('login-page-registration-link')
    registration_link.click()

    registration_email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    registration_password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    registration_button = chromium_page.get_by_test_id('registration-page-registration-button')

    expect(registration_email_input).to_be_visible()
    expect(registration_password_input).to_be_visible()
    expect(registration_button).to_be_visible()
