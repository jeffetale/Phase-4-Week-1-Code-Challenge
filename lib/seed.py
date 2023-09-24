from faker import Faker
from lib.models import db, Restaurant, Pizza, RestaurantPizza
from random import randint
from lib import app

fake = Faker()

with app.app_context():

    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    for r in range(10):
        restaurant = Restaurant(
            name = fake.company(),
            address = fake.address()
        )
        db.session.add(restaurant)

    for p in range(10):
        pizza = Pizza(
            name = fake.word(ext_word_list = ['Margherita', 'Pepperoni', 'Hawaiian', 'BBQ Chicken'
                                              , 'Chicken Periperi', 'Chicken Tikka', 'Boerewors']),
            ingredients = fake.sentence(nb_words=10)
        )

        db.session.add(pizza)

    for rp in range(10):
        restaurant_pizza = RestaurantPizza(
            pizza_id =randint(1, 10),
            restaurant_id = randint(1, 10),
            price = randint(1, 30)
        )

        db.session.add(restaurant_pizza)

    db.session.commit()
