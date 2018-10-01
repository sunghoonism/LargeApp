# -*- coding: utf-8 -*-

# Import Form and RecaptchaField (optional)
from flask_wtf import Form # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# BooleanField # Import Form validators
from wtforms.validators import Required, EqualTo


# Define the login form (WTForms)
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])

#출처: http://hamait.tistory.com/864 [HAMA 블로그]
