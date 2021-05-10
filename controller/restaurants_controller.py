import re

import flask
from flask import Blueprint, request

from config.custom_exception import handle_not_acceptable
from service.restaurants_service import get_restaurants

restaurants_blueprint = Blueprint('restaurants', __name__)


@restaurants_blueprint.route('/restaurants', methods=['GET'])
def get_restaurants_best_matchs():
    errors = ''
    if request.args.get('name') is not None and len(request.args.get('name')) == 0:
        errors = 'Name cannot be empty'

    if request.args.get('rating') and \
            not request.args.get('rating').isnumeric() and \
            not re.match(r'^-?\d+(?:\.\d+)$', request.args.get('rating')):
        if len(errors) > 0:
            errors += '\nCustomer rating must be a number'
        else:
            errors = 'Customer rating must be a number'

    if request.args.get('distance') and \
            not request.args.get('distance').isnumeric() and \
            not re.match(r'^-?\d+(?:\.\d+)$', request.args.get('distance')):
        if len(errors) > 0:
            errors += '\nDistance must be a number'
        else:
            errors = 'Distance must be a number'

    if request.args.get('price') and \
            not request.args.get('price').isnumeric() and \
            not re.match(r'^-?\d+(?:\.\d+)$', request.args.get('price')):
        if len(errors) > 0:
            errors += '\nPrice must be a number'
        else:
            errors = 'Price must be a number'

    if request.args.get('cuisine') is not None and len(request.args.get('cuisine')) == 0:
        if len(errors) > 0:
            errors += '\nCuisine cannot be empty'
        else:
            errors = 'Cuisine cannot be empty'

    if len(errors) > 0:
        return handle_not_acceptable(errors)

    return flask.jsonify(
        get_restaurants(
            name=request.args.get('name'),
            customer_rating=float(request.args.get('rating')) if request.args.get('rating') else None,
            distance=float(request.args.get('distance')) if request.args.get('distance') else None,
            price=float(request.args.get('price')) if request.args.get('price') else None,
            cuisine_name=request.args.get('cuisine')
        )
    )
