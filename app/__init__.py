from flask import Flask


from config import Config

from .auth.routes import auth
# from .ig.routes import ig
from .models import db, User
# from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)

app.config.from_object(Config)

login = LoginManager()

# @login.user_loader
# def load_user(user_id):
#     return Customer.query.get(customer_id)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)

login.login_view = 'auth.login'

# moment = Moment(app)

app.register_blueprint(auth)

from . import routes
from . import models