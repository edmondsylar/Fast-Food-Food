# Fast-Food-fast
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) 
[![Build Status](https://travis-ci.org/edmondsylar/Fast-Food-Food.svg?branch=API)](https://travis-ci.org/edmondsylar/Fast-Food-Food)
[![Coverage Status](https://coveralls.io/repos/github/edmondsylar/Fast-Food-Food/badge.svg?branch=API)](https://coveralls.io/github/edmondsylar/Fast-Food-Food?branch=API) [![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage)](https://codeclimate.com/github/codeclimate/codeclimate/test_coverage)

> fast-food-fast is a food delivery app for a restaurant designed to fullfill the following requiremets.
## 1. Users can create an account and log in
- The application should allow user registration in instances where the user is not registered with the application/system. And also if a user is already registered with the system, he or she should be able to login to there accounts.

## 2. A user should be able to order for food.
- A registerd user should be able to order for food since the application is being designed for a restaurant.

## 3. The admin should be able to add,edit or delete the fast-food items
 - The application administartor should be able to add item in form of food, edit the added items, and also delete an item from the list

## 4. The admin should be able to see a list of fast-food items
- As an administrator, he or she should be able to see a list of the added foods that exist in the system.

## 5. A user should be able to see a history of ordered food
- A user of the application should also be able to see the history of his orders that he or she made previously.

# Features

* Users can create an account and log in. 
* Users can view all entries to their diary. 
* Users can view the contents of a diary entry. 
* Users can add or modify an entry. 
  
# API Endpoints

|  Method | Endpoint  | Description |
| --- | :--- | ---: |
| GET | `/api/v1/get/orders`  | fetches all the orders.
| GET | `/api/v1/get/orders/id`  | Gets an order with the specifide id.
| GET | `/api/v1/`  | This is the default route returns a welcome message
| POST | `/api/v1/POST/orders`   | Creates an order.
| PUT | `//api/v1/PUT/orders/<orderId>`  | Update an order with the specified id.

#Installation.
To run this projectlocally you will need to have a few requirements installed and preferably a ***linux operating system.*** 

1. Python 
Preferably python 2.7 and usually comes pre installed with all linux distros but in cases where it isnt, you can install it from terminal using the commmand.

> ```` sudo apt-get install python2.7 ````
