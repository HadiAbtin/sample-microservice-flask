# Authentication for Company Services
Copyright 2024 hadi abtinfar <hadi.abtinfar@gmail.com>

This project creates a simple authentication service. You can create, delete, edit user. It has jwt functionality to generate token.

``` bash
# /api/v1/users --> GET # Lists all users
# /api/v1/users/<user_id> --> POST # Create user # -d '{"username": "TEST", "password": "TEST"}'

# /api/v1/jwt/token --> POST # Generate JWT token # -d '{"username": "TEST", "password": "TEST"}'
```
