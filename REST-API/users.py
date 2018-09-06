from flask import Flask, request, jsonify,json

class User:
    def __init__(self):
        self.users=[]
   
    def get_all_users(self):
        return jsonify(self.users)


    def delete_user(self,username):
        found =False
        for id, user in enumerate(self.users):
            if user["username"] == username:
                id = id
                found = True
                del self.users[id]
            return "users: {0}".format(json.dumps(self.users))
        return found


    def post_user(self,username,password):
        new_user = {}
        username = new_user['username']
        password = new_user['password']
        self.users.append(new_user)
        return json.dumps(new_user)
        

   
       
      
