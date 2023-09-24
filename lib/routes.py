from lib import db, api, app

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    pass

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    pass

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    pass

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pass

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    pass