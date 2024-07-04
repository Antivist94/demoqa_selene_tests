from selene import browser, have, command


class StudentRegistrationForm:
    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(
            timeout = 10).wait_until(have.size_greater_than_or_equal(3)
                                     )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

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

    def choose_gender(self):
        browser.element('[for="gender-radio-1"]').click()

    def input_user_phone_number(self):
        browser.element('#userNumber').type('7999321123')
        pass

    def input_subjects(self):
        browser.element('#subjectsInput').type('Comp').press_enter()
        browser.element('#subjectsInput').type('eco').press_enter()
        pass

    def choose_hobbie(self):
        browser.element('//label[@for="hobbies-checkbox-3"]').click()
        pass

    def upload_user_photo(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath("../files/photo_man.png"))

        pass

    def input_user_addres(self):
        browser.element('#currentAddress').type('QA street, 123')

        pass

    def select_state(self):
        browser.element('#react-select-3-input').type("Haryana").press_enter()

        pass

    def select_city(self):
        browser.element('#react-select-4-input').type("Panipat").press_enter()

        pass

    def submit(self):
        browser.element('#submit').click()

        pass

    def should_have_registered(self, param, param1, param2, param3, param4, param5, param6, param7, param8, param9):
        browser.element('#example-modal-sizes-title-lg').should(be.present)
        browser.element('.table').all('td').even.should(have.exact_texts
                                                        ())
        pass
