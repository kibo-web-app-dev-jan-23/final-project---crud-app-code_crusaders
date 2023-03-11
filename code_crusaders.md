# App Description

This is a Flask web application for a vehicle dealership. The app allows users to view, add, edit and delete vehicles from a SQLite database. It also allows users to order a vehicle by providing their name and email address. The application was created using Python 3 and the Flask web framework.

We have hosted the app on render, here's the live URL: https://codecrusaders.onrender.com/

## Schema

The schema of this app is defined in `models.py`. There are two tables defined:

### `vehicles:` This table stores the details of all the vehicles in the dealership. It has the following columns:

- `id:` An integer representing the unique ID of the vehicle.
- `make:` A string representing the make of the vehicle.
- `model:` A string representing the model of the vehicle.
- `year:` An integer representing the year of the vehicle.
- `range:` An integer representing the range of the vehicle.
- `price:` A float representing the price of the vehicle.
- `orders:` A relationship to the orders table.

### `orders:` This table stores the details of all the orders made by customers. It has the following columns:

- `id:` An integer representing the unique ID of the order.
- `vehicle_id:` An integer representing the ID of the vehicle being ordered. This is a foreign key referencing the id column in the vehicles table.
- `customer_name:` A string representing the name of the customer who placed the order.
- `customer_email:` A string representing the email address of the customer who placed the order.
- `order_date:` A datetime representing the date and time when the order was placed.

## Setting up

- To set up, install the dependencies using pip

```sh
pip install -r requirements.txt
```

- Run the app locally using `flask run` even thou you can also run it in debug mode.

- Visit http://localhost:5000 on the browser to see how it behaves.
