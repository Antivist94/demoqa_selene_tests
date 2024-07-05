class User:
    name = str
    last_name = str
    email = str
    gender = str
    phone = str
    day_of_birth = str
    month_of_birth = str
    year_of_birth = str
    subjects = str
    hobbies = str
    street = str
    state = str
    city = str
    state_and_city = str
    name_and_last_name = str
    photo = str
    date_of_birth = str

    def __init__(self, name, last_name, email, gender,
                 phone, day_of_birth, month_of_birth, year_of_birth,
                 subjects, hobbies, street, state, city, photo):
        self.subjects = subjects
        self.street = street
        self.state = state
        self.hobbies = hobbies
        self.year_of_birth = year_of_birth
        self.month_of_birth = month_of_birth
        self.city = city
        self.name = name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.phone = phone
        self.day_of_birth = day_of_birth
        self.photo = photo


class UserTextBox:
    name = str
    email = str
    current_address = str
    permanent_address = str

    def __init__(self, name, email, current_address, permanent_address):
        self.name = name
        self.email = email
        self.current_address = current_address
        self.permanent_address = permanent_address


user_text_box_test = UserTextBox('John',
                                 'joedoe@te.st',
                                 'Current st. 13',
                                 'Per road 31')
