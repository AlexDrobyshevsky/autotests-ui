from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.button import Button
from elements.text import Text
import allure


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-title-text', 'Title')
        self.course_button = Button(page, f'{identifier}-create-course-button', 'Button')

    @allure.step('Check visible create course toolbar. Button disabled: {is_create_course_disabled}')
    def check_visible(self, is_create_course_disabled=True):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        if is_create_course_disabled:
            self.course_button.check_disabled()
        else:
            self.course_button.check_enabled()

        self.course_button.check_visible()

    def click_create_button(self):
        self.course_button.click()
