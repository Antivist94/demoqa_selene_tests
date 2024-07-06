from modules.application import app
from modules import users


def test_practice_form_create_user():
    app.student_reg_form.register(users.user_reg_form)
    app.student_reg_form.assert_user_should_have_registered(users.user_reg_form)
