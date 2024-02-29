from os import environ

class Config:
    ENV = environ.get("COMPANY_AUTH_ENV", "production")
    DEBUG = bool(int(environ.get("COMPANY_AUTH_DEBUG", "0")))
    TESTING = bool(int(environ.get("COMPANY_AUTH_TESTING", "0")))
    SECRET_KEY = environ.get("COMPANY_AUTH_SECRET_KEY", "HARD_SECRET")
