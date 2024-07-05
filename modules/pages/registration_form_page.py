import os
from selene import browser, have, command, be


class StudentRegistrationForm:
    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout = 10).wait_until(have.size_greater_than_or_equal(3)
                                     )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.90)"')

    def scroll_down(self, position_1, position_2):
        browser.execute_script(f"window.scrollTo({position_1}, {position_2})")

    def input_first_name(self, name):
        browser.element('#firstName').type(name)

    def input_last_name(self, last_name):
        browser.element('#lastName').type(last_name)

    def input_user_email(self, user_email):
        browser.element('#userEmail').type(user_email)

    def input_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__year-select>[value = "{year}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def choose_gender(self, gender):
        browser.element(f'[name=gender][value={gender}]+label').click()

    def input_user_phone_number(self, number):
        browser.element('#userNumber').type(number)

    def input_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def choose_hobbies(self):
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_user_photo(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath("../files/photo_man.png"))

    def input_user_addres(self, address):
        browser.element('#currentAddress').type(address)

    def select_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def select_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit_form(self):
        browser.element('#submit').click()

    def assert_user_should_have_registered(self, name_and_last_name, email,
                                           gender, phone, date_of_birth, subjects,
                                           hobbies, photo, street,
                                           state_and_city):
        browser.element('#example-modal-sizes-title-lg').should(be.present)
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{name_and_last_name}',
            f'{email}',
            f'{gender}',
            f'{phone}',
            f'{date_of_birth}',
            f'{subjects}',
            f'{hobbies}',
            f'{photo}',
            f'{street}',
            f'{state_and_city}'
        ))
