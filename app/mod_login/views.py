# -*- coding: utf-8 -*-
from flask import Blueprint, Flask, render_template, flash, request

# Import module forms
from app.mod_login.forms import ReusableForm

# Import module models (i.e. User)
from app.mod_login.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_login = Blueprint('login', __name__, url_prefix='/login')

# Set the route and accepted methods
@mod_login.route('/login/', methods=['GET', 'POST'])
def login():

    # If sign in form is submitted
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        print(name, " ", email, " ", password)

        # Verify the sign in form
        if form.validate():
            flash('Hello '+name)
        else:
            flash('Error: All the form fields are required.')
    return render_template("login/login.html", form=form)

# 출처: http://hamait.tistory.com/864 [HAMA 블로그]
