from os import environ

class Config:

    ################### Application Config ###########################

    ENV = environ.get("COMPANY_AUTH_ENV", "production")
    DEBUG = bool(int(environ.get("COMPANY_AUTH_DEBUG", "0")))
    TESTING = bool(int(environ.get("COMPANY_AUTH_TESTING", "0")))
    SECRET_KEY = environ.get("COMPANY_AUTH_SECRET_KEY", "HARD_SECRET")
    TIMEZONE = environ.get("COMPANY_AUTH_TIMEZONE", "Asia/Tehran")
    JWT_ALG = environ.get("COMPANY_AUTH_JWT_ALG", "HS512")

    ################### Database Config ###########################

    SQLALCHEMY_DATABASE_URI = environ.get("COMPANY_AUTH_DATABASE_URI", None)
    SQLALCHENY_ECHO = DEBUG # Error Logs
    SQLALCHEMY_RECORD_QUERIES = DEBUG # List of Queries
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG # Man migzaram False

    ################### User Config ###########################

    USER_DEFAULT_ROLE = environ.get("COMPANY_AUTH_DEFAULT_ROLE", "user")
    USER_DEFAULT_EXPIRY_TIME = int(environ.get("COMPANY_AUTH_DEFAULT_EXPIRY_TIME", "365"))
    USER_DEFAULT_STATUS = int(environ.get("COMPANY_AUTH_DEFAULT_STATUS", "3"))
    USER_DEFAULT_TOKEN_EXPIRY_TIME = int(environ.get("COMPANY_AUTH_USER_DEFAULT_TOKEN_EXPIRY_TIME", "86400"))
    USER_ENABLED_STATUS = 1
    USER_ACTIVATED_STATUS = 2
    USER_FULL_STATUS = 3
