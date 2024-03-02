from flask import (
    Flask, jsonify, render_template, send_from_directory, request, url_for, redirect, flash
)

from utils.constants import *
from entity.models import *

from service.model_service import *
from service.forms.bus_forms import *

from flask_login import LoginManager, login_required, logout_user, login_user
from passlib.hash import pbkdf2_sha256
import os

app = Flask(__name__)

db_path = os.path.abspath(os.path.join(os.getcwd(), 'database', 'secure.db'))

# Set the Flask Secret Key
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

# Uncomment below to use SQLite3 for DB
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/sibro_coop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Please login to proceed."
login_manager.login_message_category = "warning"

# Helper lambda function
safe_upper = lambda val: val.upper() if val is not None else None

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        user = process_member_login_form(request.form)
        if user:

            # if check_password_hash(user.password, request.form.get('password')):
            print(user.password)
            if pbkdf2_sha256.verify(request.form.get('password'), user.password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash(f'Wrong password for {request.form.get("username")}.', category='info')
        else:
            flash(f'No acct. with username {request.form.get("username")}.', category='danger')
            
    return render_template('login/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        process_member_registration_form(request.form)
        return redirect(url_for('login'))

    return render_template('login/register.html')

@app.route('/')
@login_required
def index():

    total_members = Member.query.count()
    return render_template('main/dashboard.html', total_members=total_members)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have logged out.", category="success")
    return redirect(url_for('login'))

@app.route('/members')
@login_required
def view_members():

    all_members_data = Member.query.all()
    for member in all_members_data:
        input_string = member.occupation

        if input_string.strip() == "[]":
            output_list = []
        else:
            keys = input_string.strip("[]").replace("\"", "").split(", ")
            output_list = [occupationMap.get(key, 'Unknown') for key in keys]

        member.occupation = ' | '.join(output_list) if output_list else "N/A"

    return render_template('main/member_grid.html', all_members_data=all_members_data)

@app.route('/members/add')
@login_required
def add_member():
    return render_template('main/add_member.html')

@app.route('/members/view', methods=['GET'])
@login_required
def view_member_record():
    member_id = request.args.get('id')
    ref_member = Member.query.get(member_id)
    return render_template('main/view_member_record.html', ref_member=ref_member)

@app.route('/members/view/id_card', methods=['GET'])
@login_required
def view_member_coop_id_card():
    member_id = request.args.get('id')
    ref_member = Member.query.get(member_id)
    return render_template('id_card/main.html', ref_member=ref_member)


@app.route('/process_member', methods=['POST'])
@login_required
def process_member():  
    if request.method == 'POST':
        process_member_form(request.form)
        flash("New member added.", 'success')

    return redirect(url_for('add_member'))


@app.route('/grid/account_code')
@login_required
def account_code_grid():
    input_form = FAccountCode()

    return render_template('main/account_code_grid.html', account_code = AccountCode, input_form=input_form)


@app.route('/create/account_code', methods=['GET', 'POST'])
@login_required
def account_code_create():
    form = FAccountCode()
    update_id = request.args.get('id')
    if form.validate_on_submit():
        if not update_id:
            new_acc_code = AccountCode(
                code_id=form.code_id.data,
                code_desc=form.code_desc.data
            )
        else:
            new_acc_code = AccountCode.query.get_or_404(update_id)
            new_acc_code.code_id = form.code_id.data
            new_acc_code.code_desc = form.code_desc.data
        db.session.add(new_acc_code)
        db.session.commit()

    return redirect(url_for('account_code_grid'))

@app.route('/get/account_code', methods=['GET'])
@login_required
def account_code_get():
    code_db_id = request.args.get('id')
    if code_db_id:
        code = AccountCode.query.get_or_404(code_db_id)
        return jsonify(
        {
            "code_id" : code.code_id,
            "code_desc": code.code_desc
        }
    )

@app.route('/delete/account_code', methods=['GET', 'POST'])
@login_required
def account_code_delete():
    code_db_id = request.args.get('id')
    if code_db_id:
        db.session.delete(
            AccountCode.query.get_or_404(
                int(code_db_id)
            )
        )
        db.session.commit()
    
    return redirect(url_for('account_code_grid'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)