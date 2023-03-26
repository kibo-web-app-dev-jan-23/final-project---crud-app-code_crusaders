from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, Column, ForeignKey, String


# Initializing an instance of the SQLAlchemy class
db = SQLAlchemy()


# Creating a model for the vehicle_brands table on the database with foreign keys from the vehicles and orders table
ProductBrand = db.Table(
    "vehicle_brands",
    Column("car_id", ForeignKey("vehicles.id"), primary_key=True),
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
)


# Creating a model for the vehicle table on the database
class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    range = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', backref='vehicle', lazy=True, cascade='delete')


# Creating a model for the order table on the database
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey(
        'vehicles.id'), nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
