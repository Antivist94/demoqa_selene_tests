import paths
from modules.pages.registration_form_page import StudentRegistrationForm


def test_practice_form_create_user():
    registration_form = StudentRegistrationForm()
    registration_form.open()
    registration_form.input_first_name("Eugene")
    registration_form.input_last_name("Tester")
    registration_form.input_user_email("test@test.qom")
    registration_form.choose_gender("Male")
    registration_form.input_user_phone_number("7999321123")
    registration_form.input_date_of_birth("31","May", "2000")
    registration_form.input_subjects("Computer Science")
    registration_form.choose_hobbies()
    registration_form.upload_user_photo(paths.file_name)
    registration_form.input_user_addres("QA street, 123")
    registration_form.select_state("Haryana")
    registration_form.select_city("Panipat")
    registration_form.submit_form()
    registration_form.assert_user_should_have_registered(
        'Eugene Tester',
        'test@test.qom',
        'Male',
        '7999321123',
        '31 May,2000',
        'Computer Science',
        'Music',
        f'{paths.file_name}',
        'QA street, 123',
        'Haryana Panipat')

