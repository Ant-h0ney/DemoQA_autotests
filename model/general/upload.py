import os

from selene.support.shared import browser


def picture(picture):
    working_dir_path = os.path.abspath('')
    picture_path = os.path.join(working_dir_path, picture)
    browser.element('#uploadPicture').send_keys(picture_path)
