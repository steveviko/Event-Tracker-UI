class SignUp():
    def __init__(self):
        self.user_details = dict()


    def add(self,username,password):
        self.user_details[username] = password

    def get_password(self,username):
        return self.user_details[username]