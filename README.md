# Restaurant-Pizza API

This is a Flask-RESTful API for managing restaurants and pizzas.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed:
- Python 3.10 or later.
- Visual Studio Code or an IDE of your choice.
- Postman or Insomnia

### Installing
1. Clone the repository:

```bash
git clone https://github.com/jeffetale/Phase-4-Week-1-Code-Challenge.git
```
* Run a virtual environment:
```bash
pipenv shell
```
* Install the dependencies:
```bash
pip install -r requirements.txt
```
* Navigate to the project code:
```bash
cd Phase-4-Week-1-Code-Challenge
```
* Run the application:
```bash
python run.py
```
and click on the link created in the terminal e.g http://127.0.0.1:3000   or access the deployed link which is https://p-4-week-1-challenge.onrender.com/
* Running the tests
Run the automated tests for this system using Postman or Insomnia.

### API Endpoints
* GET /restaurants: Returns a list of all restaurants.
* GET /restaurants/<int:id>: Returns a single restaurant by ID.
* DELETE /restaurants/<int:id>: Deletes a single restaurant by ID.
* GET /pizzas: Returns a list of all pizzas.
* GET /pizzas/<int:id>: Returns a single pizza by ID.
* GET /restaurant_pizzas: Returns a list of all restaurant-pizza relationships.
* POST /restaurant_pizzas: Adds a new restaurant and pizza to the list.

### Web Browser Interaction
You can view a json response of all the resstaurants, pizzas and the restaurant-pizza relationships on the web browser by visiting https://p-4-week-1-challenge.onrender.com/

* https://p-4-week-1-challenge.onrender.com/restaurants - Get all the restaurants. Add an id at the end of the url to get a single restaurant.
* https://p-4-week-1-challenge.onrender.com/pizzas - Get all the pizzas. Add an id at the end of the url to get a single pizza.
* https://p-4-week-1-challenge.onrender.com/restaurant_pizzas - Get all the restaurant-pizzas relationships.


### Built With
- Flask - The web framework used.
- Flask_SQLAlchemy - SQL Toolkit and ORM.

### Authors
Jeff Etale - jeff.etale@moringaschool.com
