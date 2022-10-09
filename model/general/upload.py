import os

from selene.support.shared import browser


def file(type_of_file, filename):
    working_dir_path = os.path.abspath('')
    file_path = os.path.join(working_dir_path, filename)
    browser.element(f'#upload{type_of_file}').send_keys(file_path)
