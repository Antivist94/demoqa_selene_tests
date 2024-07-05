from modules.pages.registration_form_page import StudentRegistrationForm
from modules.pages.text_box_form_page import TextBoxFrom


class AppManager:
    def __init__(self):
        self.text_box_form = TextBoxFrom()
        self.left_panel = StudentRegistrationForm()


app = AppManager()
