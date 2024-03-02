from os import environ

class Config:

    ################### Application Config ###########################

    ENV = environ.get("COMPANY_AUTH_ENV", "production")
    DEBUG = bool(int(environ.get("COMPANY_AUTH_DEBUG", "0")))
    TESTING = bool(int(environ.get("COMPANY_AUTH_TESTING", "0")))
    SECRET_KEY = environ.get("COMPANY_AUTH_SECRET_KEY", "HARD_SECRET")
    TIMEZONE = environ.get("COMPANY_AUTH_TIMEZONE", "Asia/Tehran")

    ################### Database Config ###########################

    SQLALCHEMY_DATABASE_URI = environ.get("COMPANY_AUTH_DATABASE_URI", None)
    SQLALCHENY_ECHO = DEBUG # Error Logs
    SQLALCHEMY_RECORD_QUERIES = DEBUG # List of Queries
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG # Man migzaram False

    ################### User Config ###########################

    USER_DEFAULT_ROLE = environ.get("COMPANY_AUTH_DEFAULT_ROLE", "user")
    USER_DEFAULT_EXPIRY_TIME = int(environ.get("COMPANY_AUTH_DEFAULT_EXPIRY_TIME", "365"))
    USER_DEFAULT_STATUS = int(environ.get("COMPANY_AUTH_DEFAULT_STATUS", "3"))
