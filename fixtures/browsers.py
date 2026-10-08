import pytest
from playwright.sync_api import Page, Playwright

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage


@pytest.fixture
def chromium_page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()


@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    registration_page.registration_form.fill(email='user.name@gmail.com', username='username', password='password')
    registration_page.registration_form.click_registration_button()

    dashboard_page = DashboardPage(page=page)
    dashboard_page.dashboard_toolbar_view.check_visible()

    context.storage_state(path='browser-state.json')
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()
    yield page
    browser.close()
