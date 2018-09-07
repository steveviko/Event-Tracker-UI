from flask import Flask, request, jsonify,json

class Person(object):

    def __init__(self, name,age,profession,message):
        self.name = name
        self.profession = profession
        self.message = message
  
    def comment(self):
        return "user comment {} ".format(self.message)

    def get_profession(self):
        return "The person by tha name of {} is of {}profession".format(self.name,self.profession)

class User(Person):
    user_list=[]
    def __init__(self, name,age,profession,message,role):
        super().__init__(name,age,profession,message)
        self.role = role
  

    def add_users(self,user_info):
        user_info["name"] = len(self.user_list)+1
        self.user_list.append(user_info)
        return self.user_list


    def delete(self):
        del_user =self.user_list[-1]
        self.user_list.remove(del_user)
        return del_user

    def get_user(self):
        return self.user_list

class GuestList:
    def __init__(self):
        self.list_of_guest =dict()

    def add_guest(self,name):
        self.list_of_guest[name]

    def find_quest_by_name(self ,name):        
        return self.list_of_guest[name]

    def delete_guest(self, name):
        guest = [g for g in self.list_of_guest if g[name]==name]       
        self.list_of_guest.remove(guest[0])
        return jsonify({"guest_lists":self.list_of_guest})