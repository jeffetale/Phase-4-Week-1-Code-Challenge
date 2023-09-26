from flask import request
from flask_restful import Resource, reqparse
from lib.models import db, Restaurant, Pizza, RestaurantPizza
from lib.serializer import serialize_restaurant, serialize_pizza, serialize_restaurant_pizza
from lib import db, api

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('address')
parser.add_argument('ingredients')
parser.add_argument('price')
parser.add_argument('pizza_id')
parser.add_argument('restaurant_id')

class Home(Resource):
    def get(self):
        return {"Restaurant-Pizza API":
              "Get json data of available restaurants, pizzas and their relations."
               }
class RestaurantList(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        return ([serialize_restaurant(restaurant) for restaurant in restaurants])

class RestaurantData(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(int(id))

        if restaurant:
            return serialize_restaurant(restaurant), 200
        else:
            return {"message": "Restaurant not found"}, 404
        
    def delete(self, id):
        restaurant = Restaurant.query.get(int(id))
        if restaurant is None:
            return {"error": "Restaurant not found"}, 404

        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()

        return '{"message": "Restaurant deleted successfully"}', 204
    

class PizzaList(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        return ([serialize_pizza(pizza) for pizza in pizzas])

class PizzaData(Resource):
    def get(self, id):
        pizza = Pizza.query.get(int(id))

        if pizza:
            return serialize_pizza(pizza), 200
        else:
            return {"message": "Pizza not found"}, 404

class RestaurantPizzaList(Resource):
    def get(self):
        restaurant_pizzas = RestaurantPizza.query.all()
        return ([serialize_restaurant_pizza(restaurant_pizza) for restaurant_pizza in restaurant_pizzas])

class RestaurantPizzaData(Resource):
    def post(self):
        data = request.get_json()

        pizza = Pizza.query.get(data['pizza_id'])
        restaurant = Restaurant.query.get(data['restaurant_id'])

        if pizza is None or restaurant is None:
            return {"errors": ["validation errors"]}, 400

        restaurant_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )

        db.session.add(restaurant_pizza)
        db.session.commit()

        return serialize_pizza(pizza), 201

api.add_resource(Home, '/')    
api.add_resource(RestaurantList, "/restaurants")
api.add_resource(RestaurantData, "/restaurants/<int:id>")
api.add_resource(PizzaList, "/pizzas")
api.add_resource(PizzaData, "/pizzas/<int:id>")
api.add_resource(RestaurantPizzaList, "/restaurant_pizzas")
api.add_resource(RestaurantPizzaData, "/restaurant_pizzas")