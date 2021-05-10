from flask import Blueprint
from flask_restplus import Api
from documented_endpoints.restaurants_docs import namespace as restaurants_ns
"""
This file is a default file for the supported html 
Consist in a blueprint tell the name of the file you can load.
api_extension is a default config for our documentation page.
"""
blueprint = Blueprint('documented_api', __name__)

api_extension = Api(
    blueprint,
    title='Best Match Restaurants',
    version='1.0',
    description='Application to help you find the best restaurant near to you.',
    doc='/'
)

api_extension.add_namespace(restaurants_ns)
