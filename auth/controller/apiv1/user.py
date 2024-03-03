from flask import request
from auth.util import jsonify
from auth.model import User
from auth.schema.apiv1 import UserSchema
from auth.auth import db

class UserController:
    
    def get_user():
        if request.content_type != "application/json":
            return jsonify(status=415, code=101)
        try:
            users = User.query.all()
        except Exception as e:
            return jsonify(status = 500, code = 102)
        user_schema = UserSchema(many=True)
        return jsonify({"users": user_schema.dump(users)})
    def get_users(user_id):
        return jsonify(status=501, code=107)

    def create_user():
        if request.content_type != "application/json":
            return jsonify(status=415, code=101)
        user_schema = UserSchema(only=["username", "password"])
        try:
            user_data = user_schema.load(request.get_json())
        except Exception as e:
            return jsonify(status=400, code=104)
        if not user_data.get("username") or not user_data.get("password"):
            return jsonify(status=400, code=105)
        try:
            user = User.query.filter_by(username = user_data.get("username")).first()
        except Exception as e:
            return jsonify(status = 500, code = 102)
        if user is not None:
            return jsonify(status=409, code=106)
        user = User(username=user_data.get("username"), password=user_data.get("password"))
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify(status = 500, code = 102)
        user_schema = UserSchema()
        return jsonify({"user": user_schema.dump(user)}, status=201)
