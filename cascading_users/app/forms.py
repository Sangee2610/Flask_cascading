from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    add_user = SubmitField('Add user')
    remove_user = SubmitField('Remove user')
    submit = SubmitField('submit')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        print("\n\n\nuser",user)
        if user is not None:
            raise ValidationError('Please use a different username.')
