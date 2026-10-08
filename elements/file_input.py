from elements.base_element import BaseElement
import allure


class FileInput(BaseElement):
    @property
    def type_of(self):
        return 'File input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        with allure.step('Set file "{file}" to the {self.type_of} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
