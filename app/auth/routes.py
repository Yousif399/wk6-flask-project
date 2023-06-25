from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import RegisterForm, LoginForm
from ..models import User


auth = Blueprint('auth', __name__, template_folder='auth_templates')

