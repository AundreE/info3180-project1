import datetime
from . import db
class UserProfile(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80))
    lname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    location = db.Column(db.String(80))
    bio = db.Column(db.String(200))
    photo = db.Column(db.String(75))
    created_on = db.Column(db.String(10))

    __tablename__ = "UserProfile"
    
    def __init__(self,userid,fname,lname,gender,email,location,bio,photo,created_on):
        self.userid = userid
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.photo = photo
        self.created_on = created_on
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
