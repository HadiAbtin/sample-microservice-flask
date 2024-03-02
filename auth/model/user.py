from uuid import uuid4
from auth.auth import db
from auth.util import now, user_expires_at

class User(db.Model):
    id = db.Column(db.String(64), primary_key=True, default=lambda : uuid4().hex)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(128), nullable=False, default=)
    created_at = db.Column(db.Datetime, nullable=False, default=)
    expires_at = db.Column(db.Datetime, nullable=False, default=)
    last_login_at = db.Column(db.Datetime, nullable=False, default=)
    last_active_at = db.Column(db.Datetime, nullable=False, default=)
    last_change_at = db.Column(db.Datetime, nullable=False, default=)
    failed_auth_at = db.Column(db.Datetime, nullable=False, default=)
    failed_auth_count = db.Column(db.Integer, nullable=False, default=)
    status = db.Column(db.Integer, nullable=False, default=)
