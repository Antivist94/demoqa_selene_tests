from selene import browser, be, have
import os


def test_practice_form_create_user():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Eugene')
    browser.element('#lastName').type('Tester')
    browser.element('#userEmail').type('test@test.qom')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('7999321123')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select>option:nth-child(6)').click()
    browser.element('.react-datepicker__year-select>[value = "2000"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').type('Comp').press_enter()
    browser.element('#subjectsInput').type('eco').press_enter()
    browser.element('//label[@for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath("files/photo_man.png"))
    browser.element('#currentAddress').type('QA street, 123')
    browser.element('#react-select-3-input').type("Haryana").press_enter()
    browser.element('#react-select-4-input').type("Panipat").press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(be.present)
    browser.element('.table').all('td').even.should(have.exact_texts
                                                    ('Eugene Tester', 'test@test.qom', 'Male',
                                                     '7999321123', '31 May,2000', 'Computer Science, Economics',
                                                     'Music', 'photo_man.png', 'QA street, 123', 'Haryana Panipat'))
