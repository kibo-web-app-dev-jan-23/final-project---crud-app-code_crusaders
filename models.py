from app import db

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    range = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', backref='vehicle', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=False)
    customer_name = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(50), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
