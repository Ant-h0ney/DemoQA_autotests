import allure
from allure_commons.types import AttachmentType
from selene.support.shared import browser


class Attach:
    @staticmethod
    def screenshot():
        screen = browser.driver.get_screenshot_as_png()
        allure.attach(
            screen,
            name='screenshot',
            attachment_type=AttachmentType.PNG,
        )

    @staticmethod
    def logs():
        logfile = ''.join(
            f'{text}\n' for text in browser.driver.get_log(log_type='browser')
        )
        allure.attach(
            logfile,
            name='browser_log',
            attachment_type=AttachmentType.TEXT,
        )

    @staticmethod
    def html():
        source = browser.driver.page_source
        allure.attach(
            source,
            name='HTML',
            attachment_type=AttachmentType.HTML,
        )


attach = Attach()
