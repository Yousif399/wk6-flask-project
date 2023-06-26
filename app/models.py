from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


cart = db.Table(
    'cart',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False),
    db.Column('product_id',db.Integer, db.ForeignKey('product.id'), nullable=False)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False, unique=True)
    product = db.relationship('Product', backref='Product', lazy=True)

    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    weight = db.Column(db.Integer)
    price = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    added = db.relationship('User',
            secondary = 'cart',
            backref = 'added',
            lazy = 'dynamic'
            )

    def __init__(self,customer_id,title,description,weight,price):
        self.customer_id = customer_id
        self.title = title
        self.description = description
        self.weight = weight
        self.price = price
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def add_it(self,user):
        self.added.append(user)
        db.session.commit()

    def remove_it(self,user):
        self.added.remove(user)
        db.session.commit()