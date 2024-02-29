from auth.util import jsonify

class UserController:
    
    def get_users():
        return jsonify(state=501, code=107)

    def get_user(user_id):
        return jsonify(state=501, code=107)

