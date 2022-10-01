import os
import allure
from selene.support.shared import browser


@allure.step('Upload a picture {filename}')
def picture(filename):
    working_dir_path = os.path.abspath('')
    picture_path = os.path.join(working_dir_path, filename)
    browser.element('#uploadPicture').send_keys(picture_path)
