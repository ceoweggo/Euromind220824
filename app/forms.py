from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError, Length
import sqlalchemy as sa
from app import db
from app.models import User

class LoginForm (FlaskForm):
    username: StringField = StringField ("Username", validators=[DataRequired ()]);
    password: PasswordField = PasswordField ("Password", validators=[DataRequired ()]);
    rememberMe: BooleanField = BooleanField ("Remember Me");
    submit: SubmitField = SubmitField ("Sign In");

class RegistrationForm (FlaskForm):
    username: StringField = StringField ("Username", validators=[DataRequired ()]);
    email: StringField = StringField ("Email", validators=[DataRequired (), Email ()]);
    password: PasswordField = PasswordField ("Password", validators=[DataRequired ()]);
    repeatedPassword: PasswordField = PasswordField ("Repeat Password", validators=[DataRequired (), EqualTo ('password')]);
    submit: SubmitField = SubmitField ("Register");
    
    def validate_username (self, username) -> None:
        user: User = db.session.scalar (sa.select (User).where (User.username == username.data));
        if user is not None:
            raise ValidationError ("Please use different username");
    def validate_email (self, email) -> None:
        user: User = db.session.scalar (sa.select (User).where (User.email == email.data));
        if user is not None:
            raise ValidationError ("Please us different email address");
class EditProfileForm (FlaskForm):
    username: StringField = StringField ("Username", validators=[DataRequired ()]);
    about_me: TextAreaField = TextAreaField ("About me", validators=[Length (min=0, max=128)]);
    submit: SubmitField = SubmitField ("Submit");
    
    def __init__ (self, original_username, *args, **kwargs):
        super ().__init__ (*args, **kwargs);
        self.original_username = original_username;
    
    def validate_username (self, username):
        if username.data != self.original_username:
            user = db.session.scalar (sa.select (User).where (
                User.username == username.data
            ))
            if user is not None:
                raise ValidationError ("Plese use a different username")

class EmptyForm (FlaskForm):
    submit = SubmitField ("Submit");
       
class PostForm (FlaskForm):
    post = TextAreaField ("Say something", validators=[DataRequired (), Length (min = 1, max = 140)]);
    submit = SubmitField ("Submit");
