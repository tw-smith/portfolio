from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Enter your name"})
    lastname = StringField('Last Name', render_kw={"placeholder": "Enter your last name"}) #hp
    email = EmailField('Email', validators=[DataRequired(), Email()], render_kw={"placeholder": "Enter your email address."})
    message = TextAreaField('Message', validators=[DataRequired()], render_kw={"placeholder": "Enter your message.", "rows": 10})
    submit = SubmitField('Send Message')
