from datetime import datetime
from entity.models import User, Member, db
from werkzeug.security import generate_password_hash
from flask import flash
from passlib.hash import pbkdf2_sha256

def process_member_form(form) -> None:

    fields = [
        'firstName', 'middleName', 'lastName', 'birthAddress', 'dob', 'nationality', 'religion', 'sex',
        'civilStatus', 'curAddress', 'perAddress', 'contactNum', 'zipCode', 'tinNumber', 'idType1', 'idType2',
        'idNumber1', 'idNumber2', 'basicEduc', 'vocDegree', 'colDegree', 'posDegree'
    ]

    occupation = [x.upper() for x in form.getlist('occupation')]

    # Create member objects from the list of fields
    try:
        target_member = Member(
            **{field: form.get(field) if field != 'dob' else datetime.fromisoformat(form.get(field)).date()
            for field in fields},
            occupation=str(occupation)
        )

        db.session.add(target_member)
        db.session.commit()
        flash("New member added.", "success")    

    except:
        flash("An error occured.", "error")    

    
def process_member_registration_form(form) -> None:

    form_username = form.get('username')
    form_password = form.get('password')
    form_email = form.get('email')
    
    # hashed_pwd = generate_password_hash(form_password, method='pbkdf2:sha256')
    hashed_pwd = pbkdf2_sha256.hash(form_password)

    new_user = User(
        username=form_username,
        email=form_email,
        password=hashed_pwd
    )

    db.session.add(new_user)
    db.session.commit()

def process_member_login_form(form) -> User:
        form_username = form.get('username')
        user = User.query.filter_by(username=form_username).first()
        return user
