from flask_wtf import FlaskForm
from wtforms import *

class FAccountCode(FlaskForm):
    code_id = IntegerField(label="Code ID", id="code-id")
    code_desc = StringField(label="Code Description", id="code-desc")
    submit = SubmitField('Create Account Code')

    