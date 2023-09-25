# Restaurant-Pizza API

This is a Flask-RESTful API for managing restaurants and pizzas.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed:

- Python 3.10 or later.
- Visual Studio Code or an IDE of your choice.


### Installing

1. Clone the repository:

```bash
git clone https://github.com/jeffetale/Phase-4-Week-1-Code-Challenge.git

Copy
Run a virtual environment:
pipenv shell

Install the dependencies:
pip install -r requirements.txt

Navigate to the project code:
cd Phase-4-Week-1-Code-Challenge
cd lib

Copy
Run the application:
python run.py

Copy
Running the tests
Run the automated tests for this system.

API Endpoints
GET /restaurants: Returns a list of all restaurants.
GET /restaurants/<int:id>: Returns a single restaurant by ID.
DELETE /restaurants/<int:id>: Deletes a single restaurant by ID.
GET /pizzas: Returns a list of all pizzas.
GET /pizzas/<int:id>: Returns a single pizza by ID.
GET /restaurant_pizzas: Returns a list of all restaurant-pizza relationships.
POST /restaurant_pizzas: Adds a new restaurant and pizza to the list.

Built With
Flask - The web framework used
Flask_SQLAlchemy - SQL Toolkit and ORM

Authors
Jeff Etale - jeff.etale@moringaschool.com
