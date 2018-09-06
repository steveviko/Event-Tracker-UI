from flask import Flask, request, jsonify,json
from users import User


app = Flask(__name__)

users = User()

@app.route("/api/get-users", methods=['GET'])
def get_all_users():
    return users.get_all_users()

@app.route("/api/add", methods=['POST'])
def add_users():
    return users.post_user(username="",password="")

@app.route("/api/delete/<string:username>", methods=['DELETE'])
def delete_user():
    return users.delete_user()

if __name__=='__main__':
    app.run(debug=True)