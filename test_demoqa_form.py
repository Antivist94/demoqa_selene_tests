from selene import browser, be, have
import os


def test_practice_form_create_user():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Eugene').press_tab()
    browser.element('#lastName').type('Tester').press_tab()
    browser.element('//input[@id="userEmail"]').type('test@test.qom')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('//input[@id="userNumber"]').type('7999321123')
    browser.element('#dateOfBirthInput').click()
    browser.element('//select[@class="react-datepicker__month-select"]//option[@value="0"]').click()
    browser.element('//select[@class="react-datepicker__year-select"]//option[@value="2000"]').click()
    browser.element('//div[@class="react-datepicker__day react-datepicker__day--031"]').click()
    browser.element('#subjectsInput').type('Comp').press_enter()
    browser.element('#subjectsInput').type('eco').press_enter()
    browser.element('//label[@for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath("files/photo_man.png"))
    browser.element('[id="currentAddress"]').type('QA street, 123')
    browser.element('[id="react-select-3-input"]').type("Haryana").press_enter()
    browser.element('[id="react-select-4-input"]').type("Panipat").press_enter()
    browser.element('[id="submit"]').click()
    browser.element('[id="example-modal-sizes-title-lg"]').should(be.present)
    browser.element('.table').all('td').even.should(have.exact_texts
                                                    ('Eugene Tester', 'test@test.qom', 'Male', '7999321123',
                                                     '31 January,2000', 'Computer Science, Economics', 'Music',
                                                     'photo_man.png', 'QA street, 123', 'Haryana Panipat'))
