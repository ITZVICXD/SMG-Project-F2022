from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from website import app

#class Note(db.Model):#this is an example data feature from the tutorial
 #   id = db.Column(db.Integer, primary_key=True)
  #  data = db.Column(db.String(100000))
  #  date = db.Column(db.DateTime(timezone=True), default=func.now())
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))    

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    #notes = db.relationship('Note')
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
    
    def is_active(self):
        return True
    
    def is_authenticated(self):
        return self.authenticated
    
    def get_id(self):
        return self.email
    
    def is_anonymous(self):
        return False

with app.app_context():
    from . import auth 
    db.create_all()


