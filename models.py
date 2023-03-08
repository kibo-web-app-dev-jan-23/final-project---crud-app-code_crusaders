from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Integer, Column, ForeignKey, String
from flask_migrate import Migrate


app = Flask(__name__)

db = SQLAlchemy()
migrate = Migrate(app, db)


ProductBrand = db.Table(
    "vehicle_brands",
    Column("car_id", ForeignKey("vehicles.id"), primary_key=True),
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
)


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    range = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', backref='vehicle', lazy=True)

    def __init__(self, make, model, year, range, price, orders):
        self.name = make
        self.model = model
        self.year = year
        self.range = range
        self.price = price
        self.orders = orders

    def __repr__(self):
        return f"<Vehicles {self.name}>"


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey(
        'vehicles.id'), nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, vehicle_id, customer_name, customer_email, order_date):
        self.vehicle_id = vehicle_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.order_date = order_date

    def __repr__(self):
        return f"<Orders {self.name}>"
