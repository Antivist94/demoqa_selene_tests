import allure
from allure_commons.types import Severity

import paths
from modules.pages.registration_form_page import StudentRegistrationForm
from modules.users import User

@allure.tag("UI")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Evdokimenko")
@allure.feature("Форма регистрации")
@allure.story("Заполнение формы регистрации demoqa")
@allure.link("https://demoqa.com", name="Testing")
def test_practice_form_create_user():
    with allure.step('Открыть форму регистрации https://demoqa.com/automation-practice-form'):
        registration_form = StudentRegistrationForm()
    user = User(name = 'Eugene', last_name = 'Tester', email = 'test@test.qom',
                gender = 'Male',
                phone = '7999321123',
                day_of_birth = '31',
                month_of_birth = 'May',
                year_of_birth = '2000',
                subjects = 'Computer Science',
                hobbies = 'Music',
                street = 'QA street, 123',
                state = 'Haryana',
                city = 'Panipat',
                photo = paths.file_name)
    with allure.step('Заполнить данные по пользователю и подтвердить регистрацию'):
        registration_form.register(user)
    with allure.step('ASSERT: Введенные данные пользователя отображаются в таблице'):
        registration_form.assert_user_should_have_registered(user)
