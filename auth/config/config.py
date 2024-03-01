from os import environ

class Config:

    ################### Application Config ###########################

    ENV = environ.get("COMPANY_AUTH_ENV", "production")
    DEBUG = bool(int(environ.get("COMPANY_AUTH_DEBUG", "0")))
    TESTING = bool(int(environ.get("COMPANY_AUTH_TESTING", "0")))
    SECRET_KEY = environ.get("COMPANY_AUTH_SECRET_KEY", "HARD_SECRET")

    ################### Database Config ###########################

    SQLALCHEMY_DATABASE_URI = environ.get("COMPANY_AUTH_DATABASE_URI", None)
    SQLALCHENY_ECHO = DEBUG # Error Logs
    SQLALCHEMY_RECORD_QUERIES = DEBUG # List of Queries
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG # Man migzaram False

