from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, TextAreaField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired, Email
from app import allowed_extensions

class SignUpForm(FlaskForm):
    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    gender = SelectField(label='Gender', choices=[("Male", "Male"), ("Female", "Female")])
    email = StringField('Email', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    biography = StringField('Biography', validators=[InputRequired()])
    photo = FileField("Profile Picture", validators=[FileRequired(), FileAllowed(allowed_extensions, ''.join( item+" " for item in allowed_extensions)+"only")])

    

    
