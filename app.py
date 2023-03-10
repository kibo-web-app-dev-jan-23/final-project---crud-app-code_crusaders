from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Vehicle, Order
from datetime import datetime

# Creating a new instance of a Flask web application
app = Flask(__name__)

# configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the app with the extension
db.init_app(app)


##################
# Application routes
##################

# Defining a route for the root URL
@app.route('/')
def index():
    db.create_all()
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)


# Creating a route map to the '/vehicles/new' URL endpoint
@app.route('/vehicles/new', methods=['GET', 'POST'])
def new_vehicle():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        range = request.form['range']
        price = request.form['price']
        vehicle = Vehicle(make=make, model=model, year=year,
                          range=range, price=price)
        db.session.add(vehicle)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_vehicle.html')


# Creating a route to handle the editting of a single item
@app.route('/vehicles/<int:id>/edit', methods=['GET', 'POST'])
def edit_vehicle(id):
    vehicle = Vehicle.query.get(id)
    if request.method == 'POST':
        vehicle.make = request.form['make']
        vehicle.model = request.form['model']
        vehicle.year = request.form['year']
        vehicle.range = request.form['range']
        vehicle.price = request.form['price']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_vehicle.html', vehicle=vehicle)


# Creating a route to handle the deleting of a individual item
@app.route('/vehicles/<int:id>/delete', methods=['POST'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    return redirect(url_for('index'))


# Creating a route to handle the ordering of a vehicles
@app.route('/vehicles/<int:id>/orders', methods=['GET', 'POST'])
def vehicle_orders(id):
    vehicle = Vehicle.query.get(id)
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        order = Order(vehicle_id=id, customer_name=customer_name,
                      customer_email=customer_email, order_date=datetime.now())
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('index'))
    orders = Order.query.filter_by(vehicle_id=id).all()
    return render_template('vehicle_orders.html', vehicle=vehicle, orders=orders)


# Run the app in debug mode if this file is run
if __name__ == "__main__":
    app.run(debug=True)
