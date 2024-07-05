import script_os
from modules.pages.registration_form_page import StudentRegistrationForm
from modules.users import User


def test_practice_form_create_user():
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
                photo = script_os.file)
    registration_form.register(user)
    registration_form.assert_user_should_have_registered(user)
