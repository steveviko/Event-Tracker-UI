class Person(object):

    def __init__(self, name,age,profession,message):
        self.name = username
        self.profession = profession
        self.message = message
  
    def comment(self):
        return "user comment {} ".format(self.message)

    def post(self):
        return "you have successfully added a post"

class User(Person):

    def __init__(self, name,age,profession,message):
        super().__init__(name,age,profession,message,role)
        self.role = role


    def delete(self):
        return "Admin has successfully deleted {}".format(super().comment())

    def edit(self):
        pass

class GuestList:
    def __init__(self):
        self.list_of_guest ={}

    def add_guest(self,guest):
        if(self.guest_exists(guest.id)):
            pass

        slef.guest_dict[guest.id]=guest

    def find_quest_by_id(self ,id):
        if(self.guest_exists(id)):
            return self.guest_dict[id]
        return None


    def guest_exists(self, id):
        return self.guest_dict.__contains__(id)

    def delete_guest(self, id):
        pass