import re

class SignUp():
    def __init__(self):
        self.user_details = dict()


    def add(self,username,password,email):
        self.user_details[username] = password

    def user_num_list(self,username):
        return [x for x in range(username)]

    @staticmethod
    def validate_email(email):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        else:
            return email