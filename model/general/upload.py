import os

from selene.support.shared import browser


class Upload:
    def __init__(self, name: str):
        self.name = name

    def file(self, filename):
        working_dir_path = os.path.abspath('')
        file_path = os.path.join(working_dir_path, filename)
        browser.element(f'#upload{self.name}').send_keys(file_path)
