from flask import Flask, jsonify, request, render_template
from database import *
from account import BankAccount
from utils import *
import secrets


## active sessions need expiry
active_sessions = {}
app = Flask(__name__)


@app.route("/")
def hello():
    return jsonify({"message": "hello world"})


@app.route("/ping")
def ping():
    return jsonify({"status": "pong"})


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    fullname = data["fullname"]
    address = data["address"]
    email = data["email"]

    if db_userexistence(username):
        return jsonify({"error": "username already taken"}), 400

    else:
        new_user = BankAccount(
            username, fullname, address, email, hash_password(password)
        )
        db_insert(new_user)
        return jsonify({"message": "registered successfully"}), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    if db_passwordcheck(username, password):
        token = secrets.token_hex(32)
        active_sessions[token] = username
        return jsonify({"token": token}), 200

    else:
        return jsonify({"error": "wrong password"}), 401


@app.route("/balance", methods=["GET"])
def balance():
    token = request.headers.get("Authorization")

    if token not in active_sessions:
        return jsonify({"error": "unauthorized"}), 401

    username = active_sessions[token]
    user = db_recreateObject(username)

    return jsonify({"balance": user.get_balance()}), 200


@app.route("/deposit", methods=["POST"])
def deposit():

    token = request.headers.get("Authorization")

    if token not in active_sessions:
        return jsonify({"error": "unauthorized"}), 401

    data = request.get_json()

    amount = data["amount"]
    username = active_sessions[token]
    user = db_recreateObject(username)

    if check_amount(amount):
        user.deposit(amount)
        db_updatebalance(user)

        return jsonify({"message": "amount deposited"}), 201
    else:
        return jsonify({"message": "invalid amount"}), 400


@app.route("/withdraw", methods=["POST"])
def withdraw():

    token = request.headers.get("Authorization")

    if token not in active_sessions:
        return jsonify({"error": "unauthorized"}), 401

    data = request.get_json()

    amount = data["amount"]
    username = active_sessions[token]
    user = db_recreateObject(username)

    if check_amountwithdrawal(amount, user):
        user.withdrawal(amount)
        db_updatebalance(user)
        return jsonify({"message": "amount withdrawn"}), 201

    else:
        return jsonify({"error": "invalid amount"}), 400


@app.route("/history", methods=["GET"])
def history():

    token = request.headers.get("Authorization")

    if token not in active_sessions:
        return jsonify({"error": "unauthorized"}), 401

    username = active_sessions[token]
    user = db_recreateObject(username)

    return jsonify({"history": print_history(user)}), 200


@app.route("/app")
def frontend():
    return render_template("index.html")

if __name__ == "__main__":
    db_init()
    app.run(debug=True)
