from flask import Flask, request, jsonify
from users import User


app = Flask(__name__)

@app.route("/api/get-users", methods=['GET'])
def get_users():
    return "ALL users"

@app.route("/api/add", methods=['POST'])
def add_users():
    return "user id"

@app.route("/api/delete", methods=['POST'])
def delete_user():
    return "del id"

if __name__=='__main__':
    app.run(debug=True)