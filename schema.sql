--Creating the vehicles table with its column
CREATE TABLE vehicles (
    id SERIAL PRIMARY KEY,
    make VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    range INTEGER NOT NULL,
    price FLOAT NOT NULL
);

--Creating the orders table with its column
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    customer_email VARCHAR(50) NOT NULL,
    order_date TIMESTAMP NOT NULL
);

--Creating the vehicle_brands table with its column related by foreign keys
CREATE TABLE vehicle_brands (
    car_id INTEGER NOT NULL REFERENCES vehicles (id),
    order_id INTEGER NOT NULL REFERENCES orders (id),
    PRIMARY KEY (car_id, order_id)
);
