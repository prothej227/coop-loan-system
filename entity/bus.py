from entity.models import db

class AccountCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code_id = db.Column(db.Integer())
    code_desc = db.Column(db.String(255))
    journals = db.relationship('Journal', backref='account_code', lazy=True)

class Journal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    payee = db.Column(db.String(255))
    tin_no = db.Column(db.String(100))
    particulars = db.Column(db.Text)  # Long varchar/String
    amount = db.Column(db.Float)  # or db.Column(db.DECIMAL(10, 2)) for decimal
    account_code_id = db.Column(db.Integer, db.ForeignKey('account_code.id'))
    debit = db.Column(db.Float)  # or db.Column(db.DECIMAL(10, 2)) for decimal
    credit = db.Column(db.Float)  # or db.Column(db.DECIMAL(10, 2)) for decimal