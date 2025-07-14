from flask import Blueprint, request, jsonify, session
from .models import User
from . import db
from werkzeug.security import check_password_hash

main = Blueprint('main', __name__)

@main.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        # Simulate session for now
        return jsonify({
            "message": "Login successful",
            "user": {
                "user_id": user.user_id,
                "username": user.username,
                "role": user.role,
                "department": user.department
            }
        })
    return jsonify({"error": "Invalid credentials"}), 401
