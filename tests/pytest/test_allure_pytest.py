import allure


@allure.step('Opening browser')
def opening_browser():
    with allure.step('Get browser'):
        ...

    with allure.step('Start browser'):
        ...


@allure.step('Creating course with title "{title}"')
def creating_course(title: str):
    ...


@allure.step('Closing browser')
def closing_browser():
    ...


def test_feature():
    opening_browser()

    creating_course(title="locust")
    creating_course(title="Pytest")
    creating_course(title="Python")
    creating_course(title="Playwright")

    closing_browser()
