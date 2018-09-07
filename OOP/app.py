from flask import Flask, request, jsonify,json
from module import Person, User,GuestList


app = Flask(__name__)

guests = GuestList()

@app.route("/api/guests", methods=['GET'])
def get_all_users():
    return "guests"

@app.route("/api/add-guest", methods=['POST'])
def add_users():
    return "guest added "

@app.route("/api/delete/<string:name>", methods=['DELETE'])
def delete_user():
    return "guest deleted"