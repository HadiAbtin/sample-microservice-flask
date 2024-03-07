
from flask import request
from auth.util import jsonify, now
from jwt import encode, decode
from auth.model import User
from auth.schema.apiv1 import UserSchema
from auth.config import Config
from time import time
from auth.auth import db
from pytz import timezone

class AuthController:
    def create_jwt_token():
        if request.content_type != "application/json":
            return jsonify(staztus=415, code=101) # Invalid media type

        user_schema = UserSchema(only=["username", "password"])
        try:
            user_data = user_schema.load(request.get_json())
        except Exception as e:
            return jsonify(status=400, code=104)

        if not user_data.get("username") or not user_data.get("password"):
            return jsonify(status=400, code=105)
        try:
            user = User.query.filter_by(username=user_data.get("username")).first() # Find user
        except Exception as e:
            return jsonify(status=500, code=102) # Database error
        if user is None:
            return jsonify(status=401, code=103 ) # Because of information disclosure
        if user.password != user_data.get("password"):
            user.failed_auth_at = now()
            user.failed_auth_count = +1
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                return jsonify(status=500, code=102) # Database error

            return jsonify(status=401, code=111 ) # Again information vulnerability
        tz = timezone(Config.TIMEZONE)
        if user.expires_at < now().astimezone(tz).replace(tzinfo=None):
            return jsonify(status=401, code=108) # User is expired

        if user.status != Config.USER_FULL_STATUS:
            return jsonify(status=401, code=109) # Bad user status
        
        current_time = time() 
        try:
            user_jwt_token = encode(
                    {
                        "sub": user.id,
                        "exp": current_time + Config.USER_DEFAULT_TOKEN_EXPIRY_TIME,
                        "nbf": current_time,
                        # 2 - "resource": "user",
                        # 1 or 3 - "user": {
                        "data": {
                            # 1 - "type": "resource",
                            # 1 - "res": "user",
                            "id": user.id,
                            "username": user.username,
                            "role": user.role
                            }
                    },
                    Config.SECRET_KEY,
                    Config.JWT_ALG
                    ).encode("utf8") # Create JWT token
        except Exception as e:
            return jsonify(status=500, code=110) # Token(signature) encryption error
        user.last_login_at = now()
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify(status=500, code=102)
        user_schema = UserSchema()
        return jsonify(
                state = {"user": user_schema.dump(user)},
                header = {"X-Subject-Token": user_jwt_token}
                ) # Return JWT token

    def verify_jwt_token():
        return jsonify(status=501, code=107)
