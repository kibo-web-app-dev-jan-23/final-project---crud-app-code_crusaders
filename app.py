from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Vehicle, Order
from datetime import datetime

app = Flask(__name__)

# configure the SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Faqeeh123@localhost:5432/electric_car'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the app with the extension
db.init_app(app)


@app.route('/')
def index():
    db.create_all()
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)


@app.route('/vehicles/new', methods=['GET', 'POST'])
def new_vehicle():
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        range = request.form['range']
        price = request.form['price']     
        vehicle = Vehicle(make=make, model=model, year=year, range=range, price=price)
        db.session.add(vehicle)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_vehicle.html')


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


@app.route('/vehicles/<int:id>/delete', methods=['POST'])
def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)
    db.session.delete(vehicle)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/vehicles/int:id/orders', methods=['GET', 'POST'])
def vehicle_orders(id):
    vehicle = Vehicle.query.get(id)
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        order = Order(vehicle_id=id, customer_name=customer_name,
                      customer_email=customer_email, order_date=datetime.now())
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('vehicle_orders', id=id))
    orders = Order.query.filter_by(vehicle_id=id).all()
    return render_template('vehicle_orders.html', vehicle=vehicle, orders=orders)


if __name__ == "__main__":
    app.run(debug=True)
