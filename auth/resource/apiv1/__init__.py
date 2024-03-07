from auth.auth import apiv1 as api
from auth.resource.apiv1.user import UserResource
from auth.resource.apiv1.jwt import AuthResource

api.add_resource(
        AuthResource,
        "/auth/tokens",
        methods = ["GET", "POST"],
        endpoint = "jwt_tokens"
        )

api.add_resource(
        UserResource,
        "/users",
        methods = ["GET", "POST"],
        endpoint = "users"
        )

api.add_resource(
        UserResource,
        "/users/<user_id>",
        methods = ["GET", "POST", "PATCH", "DELETE"],
        endpoint = "user"
        )
