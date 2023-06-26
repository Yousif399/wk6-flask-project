from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import Signup, Login
# from ..models import User
from ..myfunctions import Amiibo
from flask_login import current_user, login_user, logout_user
from werkzeug.security import check_password_hash


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/register')
def register():
    return render_template('register.html')