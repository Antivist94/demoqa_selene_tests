from modules import users
from modules.application import app


def test_text_box_form():
    app.left_panel.open_text_box_form()
    app.text_box_form.register_text_box(users.user_text_box_test)
    app.text_box_form.assert_text_box_output_get_user_info(users.user_text_box_test)
