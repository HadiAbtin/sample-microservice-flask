from auth.util import jsonify

class UserController:
    
    def get_user():
        return jsonify(status=501, code=107)

    def get_users(user_id):
        return jsonify(status=501, code=107)

