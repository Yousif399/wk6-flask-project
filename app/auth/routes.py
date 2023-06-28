from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import Signup, Login
from ..models import User
from ..myfunctions import Amiibo
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login', methods= ["POST","GET"])
def login():
    form = Login()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password,password):
                    flash(f"welcome back {username}", "success")
                    print('welcome')
                    return redirect(url_for('products'))
    return render_template('login.html',form=form)

@auth.route('/register', methods=["POST", "GET"])
def register():
    form = Signup()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User(username,email,password)
            user.save_user()
            print(user)
            return redirect(url_for('auth.login'))
             

    
    return render_template('signup.html',form=form)