from flask_login import  UserMixin
from flask_sqlalchemy  import SQLAlchemy


db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Member(db.Model):
    member_id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(255))
    middleName = db.Column(db.String(255))
    lastName = db.Column(db.String(255))
    birthAddress = db.Column(db.String(50))
    dob = db.Column(db.Date)
    nationality = db.Column(db.String(255))
    religion = db.Column(db.String(255))
    sex = db.Column(db.String(6))
    civilStatus = db.Column(db.String(50))
    curAddress = db.Column(db.String(255))
    perAddress = db.Column(db.String(255))
    contactNum = db.Column(db.String(20))
    zipCode = db.Column(db.String(10))
    tinNumber = db.Column(db.String(40))
    idType1 = db.Column(db.String(25))
    idType2 = db.Column(db.String(25))
    idNumber1 = db.Column(db.String(30))
    idNumber2 = db.Column(db.String(30))
    basicEduc = db.Column(db.String(255))
    vocDegree = db.Column(db.String(255))
    colDegree = db.Column(db.String(255))
    posDegree = db.Column(db.String(255))
    occupation = db.Column(db.String(10))
    beneficiary = db.relationship('Beneficiary', backref='member')

class Beneficiary(db.Model):
    ben_id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.member_id'))
    full_name = db.Column(db.String(255))
    relationship = db.Column(db.String(255))
    dob = db.Column(db.Date)
    occupation = db.Column(db.String(255))
    employer = db.Column(db.String(255))

# ---------------- Business Entities ---------------- 
class AccountCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_id = db.Column(db.Integer())
    code_desc = db.Column(db.String(255))
    journals = db.relationship('Journal', backref='account_code', lazy=True)
    
    @classmethod
    def get_labels(cls) -> list:
        return ["ID", "Code ID", "Code Description"]
    

    
class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    date = db.Column(db.Date)
    payee = db.Column(db.String(255))
    tin_no = db.Column(db.String(100))
    particulars = db.Column(db.Text)  # Long varchar/String
    amount = db.Column(db.Float)  # or db.Column(db.DECIMAL(10, 2)) for decimal
    account_code_id = db.Column(db.Integer, db.ForeignKey('account_code.id'))
    debit = db.Column(db.Float)  # or db.Column(db.DECIMAL(10, 2)) for decimal
    credit = db.Column(db.Float)  # or db.Column(db.DECIMAL(10, 2)) for decimal

    
