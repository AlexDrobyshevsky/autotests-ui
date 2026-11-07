from elements.base_element import BaseElement
import allure
from tools.playwright import logger

logger = logger.get_logger('FILE_INPUT')


class FileInput(BaseElement):
    @property
    def type_of(self):
        return 'File input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        step = 'Set file "{file}" to the {self.type_of} "{self.name}"'

        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
