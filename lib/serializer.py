def serialize_restaurant(restaurant):
    return {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [serialize_restaurant_pizza(rp) for rp in restaurant.pizzas]
    }

def serialize_pizza(pizza):
    return {
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients,
        'restaurants': [restaurant.id for restaurant in pizza.restaurants]
    }

def serialize_restaurant_pizza(restaurant_pizza):
    return {
        'id': restaurant_pizza.id,
        'pizza_id': restaurant_pizza.pizza_id,
        'restaurant_id': restaurant_pizza.restaurant_id,
        'price': restaurant_pizza.price
    }
