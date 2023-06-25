from flask import Flask


from config import Config

from .auth.routes import auth
from .models import db, User
