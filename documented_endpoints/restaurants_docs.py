from flask_restplus import Namespace, fields, Resource, reqparse

"""
Responsible for the restaurant documentation page tell what model is used and how can you filter the restaurants
"""

namespace = Namespace('restaurants', 'Restaurants related endpoints')

restaurant_model = namespace.model('Restaurant', {
    'name': fields.String(
        readonly=True,
        description="Restaurant's name"
    ),
    'customer_rating': fields.Float(
        readonly=True,
        description='Hello world message'
    ),
    'distance': fields.Float(
        readonly=True,
        description='Hello world message'
    ),
    'price': fields.Float(
        readonly=True,
        description='Hello world message'
    ),
    'cuisine_id': fields.Integer(
        readonly=True,
        description='Hello world message'
    ),
    'cuisine_name': fields.String(
        readonly=True,
        description='Hello world message'
    )
})

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help="A Restaurant Name exact or partial like Mcd or Mcdonald’s")
parser.add_argument('rating', type=str, help="A Customer Rating e.g.: 1, 2, 3, 4, 5")
parser.add_argument('distance', type=str, help="A Distance in miles from the company")
parser.add_argument('price', type=str, help="Meal cost per person e.g.: 10, 15, 20")
parser.add_argument('cuisine', type=str, help="The type of cuisine the restaurant have the name,"
                                              " could be partial or exact e.g: Chinese, Chi, Mex")

restaurant_example = [
    {
        "cuisine_id": 2,
        "cuisine_name": "Chinese",
        "customer_rating": 5.0,
        "distance": 9.0,
        "name": "Tasteful Grill",
        "price": 10.0
    },
    {
        "cuisine_id": 2,
        "cuisine_name": "Chinese",
        "customer_rating": 5.0,
        "distance": 5.0,
        "name": "Lane Tasty",
        "price": 35.0
    },
    {
        "cuisine_id": 2,
        "cuisine_name": "Chinese",
        "customer_rating": 5.0,
        "distance": 3.0,
        "name": "Gusto Delicious",
        "price": 50.0
    },
    {
        "cuisine_id": 2,
        "cuisine_name": "Chinese",
        "customer_rating": 4.0,
        "distance": 1.0,
        "name": "Deliciouszilla",
        "price": 15.0
    },
    {
        "cuisine_id": 2,
        "cuisine_name": "Chinese",
        "customer_rating": 4.0,
        "distance": 4.0,
        "name": "Hot Bar",
        "price": 20.0
    }
]


@namespace.route('')
class Restaurants(Resource):
    @namespace.marshal_with(restaurant_model, as_list=True)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(406, 'Could be one or more of this messages: '
                             'Name cannot be empty, '
                             'Customer rating must be a number, '
                             'Distance must be a number, '
                             'Price must be a number, '
                             'Cuisine cannot be empty')
    @namespace.expect(parser)
    def get(self):
        """
        Restaurants best matched list
        """
        return restaurant_example
