from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-title-text')
        self.button = page.get_by_test_id(f'{identifier}-create-exercise-button')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Exercises')

    def check_visible_button(self):
        expect(self.button).to_be_visible()

    def click_button(self):
        self.button.click()
