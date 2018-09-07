from flask import Flask, request, jsonify,json
from module import Person, User,GuestList


app = Flask(__name__)

users= User()
guests = GuestList()


@app.route("/api/add-user", methods = ["POST"])
def add_user():   
    data = {
        "name": request.json["name"],
        "role": request.json["role"]
    }
    result = [u for u in users.user_list if data["name"] == u["name"]]
    if data["name"] == "":
        return jsonify({"Error": "please fill in your name field"})
    if data["role"] == "":
        return jsonify({"Error": "fill in your role"})
    if not result:
        users.add_users(data)
        return jsonify({"User": data})
    else:
        return jsonify({"Error": "Duplicate data"})

@app.route("/api/get-users", methods = ["GET"])
def get_users():
    user_bio = users.get_user()
    return jsonify({"User info": user_bio})


@app.route("/api/delete-user", methods = ["DELETE"])
def delete_users():
    del_user= users.delete_user()
    return jsonify({"Erased": del_user})


@app.route("/api/guests", methods=['GET'])
def get_all_guests():
    return guests.find_quest_by_name()

@app.route("/api/add-guest", methods=['POST'])
def add_users():
    return guests.add_guest()

@app.route("/api/delete/<string:name>", methods=['DELETE'])
def delete_user():
    return guests.delete_guest()