"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField,
                     TextAreaField,
                     SubmitField,
                     PasswordField,
                     DateField,
                     SelectField)
from wtforms.validators import (DataRequired,
                                Email,
                                EqualTo,
                                Length,
                                URL)


class ReqForm(FlaskForm):
    """Contact form."""

    name = StringField('Name', [
        DataRequired()])
    tel = StringField('Email Address', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    address = StringField('Home Address', [
        DataRequired(),
        Length(min=4, message='Your address is too short.')])
    submit = SubmitField('Submit')

class DelForm(FlaskForm):
    """Contact form."""

    name = StringField('Name', [
        DataRequired()])
    tel = StringField('Email Address', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    address = StringField('Home Address', [
        DataRequired(),
        Length(min=4, message='Your address is too short.')])
    submit = SubmitField('Submit')
