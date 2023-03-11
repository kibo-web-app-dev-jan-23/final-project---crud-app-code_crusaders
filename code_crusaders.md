# Electric Cars

Electric cars is an applicatio that displays available vehicles for sale in a car shop.
It allows shop owners to edit displayed vehicles, view orders placed by customers and delete vehicles when they are out of stock. It also allows addition of new vehicles to the displayed items. 



## Schema tables
 The tables in schema.sql are

 - Vehicles table which cotains the information about each vehicle. It has the make, the model, the year, the range and the price columns.
 - Orders table which keeps the records of orders placed by the customers.It consists of columns for the customer name, customer email address and the order date.
 - Vehicle brands table which links the car id to the order id 

 ## Setting up
 To set up, install the dependencies using pip
 ```sh
 pip install -r requirements.txt
 ```
Run the app locally and visit http://127.0.0.1:5000 on the browser to see how it behaves.

