from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    button = page.get_by_test_id('registration-page-registration-button')
    expect(button).to_be_disabled()

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.focus()
    page.keyboard.type('user.name@gmail.com', delay=200)

    registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_username_input.focus()
    page.keyboard.type('username', delay=200)

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.focus()
    page.keyboard.type('password', delay=200)


    expect(button).not_to_be_disabled()


    page.wait_for_timeout(5000)