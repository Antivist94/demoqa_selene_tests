from selene import browser, have, command, be
from modules.users import UserTextBox


class TextBoxFrom:

    def __init__(self):
        pass

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout = 10).wait_until(have.size_greater_than_or_equal(3)
                                     )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.driver.execute_script('document.querySelector(".body-height").style.transform = "scale(.90)"')

    def open_simple_registration_form(self, text_box_from=None):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout = 10).wait_until(have.size_greater_than_or_equal(3)
                                     )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.all('.element-group').first.should(have.text('Elements')).click()
        browser.all('.menu-list .text').element_by(have.exact_text('Text Box')).click()
        return text_box_from

    def input_name(self, name):
        browser.element('#userName').type(name)
        return self

    def input_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def input_current_address(self, current_address):
        browser.element('#currentAddress').type(current_address)
        return self

    def input_permanent_address(self, permanent_address):
        browser.element('#permanentAddress').type(permanent_address)
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view)
        browser.element('#submit').click()
        return self

    def register_text_box(self, user: UserTextBox):
        self.input_name(user.name)
        self.input_email(user.email)
        self.input_current_address(user.current_address)
        self.input_permanent_address(user.permanent_address)
        self.submit()
        return self

    def assert_text_box_output_get_user_info(self, user: UserTextBox):
        browser.element('#output').should(have.exact_text(f'Name:{user.name}\n'
                                                          f'Email:{user.email}\n'
                                                          f'Current Address :{user.current_address}\n'
                                                          f'Permananet Address :{user.permanent_address}'))
        return self
