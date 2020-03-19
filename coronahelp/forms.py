
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
        DataRequired()])
    body = TextAreaField('Message', [
        DataRequired(),
        Length(min=4, message='Your message is too short.')])
    submit = SubmitField('Submit')
