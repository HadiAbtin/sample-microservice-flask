from flask_restful import Resource
from auth.controller.apiv1 import UserController
class UserResource(Resource):

    def get(self, user_id=None):
        """
        GET /users --> Get list of user
        GET /users/<user_id> --> Get user
        """
        if user_id is None:
            return UserController.get_users()
        else:
            return UserController.get_user(user_id)

    def post(self):
        """
        POST /users --> Create user
        POST /users/<user_id> --> Not Allowed
        """
        return UserController.create_user()
        pass
    def patch(self, user_id):
        """
        PATCH /users/<user_id> --> change password
        """
        return UserController.update_user(user_id)

    def delete(self, user_id):
        """
        DELETE /user/<user_id> --> delete user
        """
        return UserController.delete_user(user_id)



