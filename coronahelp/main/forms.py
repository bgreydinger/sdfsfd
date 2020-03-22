
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


class ContactForm(FlaskForm):
    """Contact form."""

    name = StringField('Name', [
        DataRequired()])
    tel = StringField('Telephone Number', [
        DataRequired(),
        Length(min=12, max=12, message='Your telephone number is invalid.')])
    address = TextAreaField('Home Address', [
        DataRequired(),
        Length(min=4, message='Your address is too short.')])
    submit = SubmitField('Submit')
