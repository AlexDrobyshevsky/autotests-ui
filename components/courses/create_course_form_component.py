from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.input import Input
from elements.textarea import TextArea


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.title = Input(page, f'{identifier}-title-input', 'Title')
        self.estimated_time = Input(page, f'{identifier}-estimated-time-input', 'Estimated_time')
        self.description = TextArea(page, f'{identifier}-description-input', 'Description')
        self.max_score = Input(page, f'{identifier}-max-score-input', 'Max score')
        self.min_score = Input(page, f'{identifier}-min-score-input', 'Min score')

    def check_visible(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.check_visible()
        self.title.check_have_value(title)

        self.estimated_time.check_visible()
        self.estimated_time.check_have_value(estimated_time)

        self.description.check_visible()
        self.description.check_have_value(description)

        self.max_score.check_visible()
        self.max_score.check_have_value(max_score)

        self.min_score.check_visible()
        self.min_score.check_have_value(min_score)

    def fill_form(self, title: str, estimated_time: str, description: str, max_score: str, min_score: str):
        self.title.fill(title)
        self.title.check_have_value(title)

        self.estimated_time.fill(estimated_time)
        self.estimated_time.check_have_value(estimated_time)

        self.description.fill(description)
        self.description.check_have_value(description)

        self.max_score.fill(max_score)
        self.max_score.check_have_value(max_score)

        self.min_score.fill(min_score)
        self.min_score.check_have_value(min_score)
