from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import Required,EqualTo
from ..models import Group

class LoginForm(FlaskForm):
    '''
    Function to create a wtf form for logging in
    '''
    name = StringField('Your Group Name', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    '''
    Function to create a wtf form for registering
    '''
    name = StringField('Enter Group Name', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo('password_confirm', message="Passwords must match")])
    password_confirm = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_name(self,data_field):
        if Group.query.filter_by(name=data_field.data).first():
            raise ValidationError('The group name is taken')




