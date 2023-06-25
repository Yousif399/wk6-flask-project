from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import Signup, Login
# from ..models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')

