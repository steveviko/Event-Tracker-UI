from flask import Flask, request, jsonify,json

users=[{"name":"steve"},{"name":"luke"},{"name":"john"}]

class User:
        
   
    def get_all_users(self):
        return jsonify(users)

    def post_user(self):
        user ={'name':request.json['name']}
        users.append(user)
        return jsonify({"users":users})

    def delete_user(self,name):
        user =[user for user in users if user['name'] == name]
        users.remove(user[0])
        return jsonify({"users":users})
    
       
        

   
       
      
