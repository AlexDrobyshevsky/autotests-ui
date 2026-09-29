from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = Text(page, f'{identifier}-title-text', 'Title')
        self.button = Button(page, f'{identifier}-create-exercise-button', 'Button')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')

    def check_visible_button(self):
        self.button.check_visible()

    def click_button(self):
        self.button.click()
