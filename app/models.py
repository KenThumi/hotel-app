from . import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    '''Class to handle user'''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index=True)
    role = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    # bio = db.Column(db.String())
    # profile_pic_path = db.Column(db.String())
    # posts = db.relationship('Post',backref = 'user',lazy="dynamic")
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    @classmethod
    def isAdmin(cls,id):
        user = cls.query.get(int(id))
        if user.role == 'admin':
            return True
        else:
            False
    def __repr__(self):
        return f'User {self.username} {self.email}'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer,primary_key = True)
    classification = db.Column(db.String(255), unique = True)
    details = db.Column(db.Text)
    cost = db.Column(db.String(255))
    units = db.Column(db.Integer)
    image = db.Column(db.Text)

    def __repr__(self):
        return f'Room {self.classification} {self.cost} {self.units}'
