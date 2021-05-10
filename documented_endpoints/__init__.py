from flask import Blueprint
from flask_restplus import Api
from documented_endpoints.restaurants_docs import namespace as restaurants_ns

blueprint = Blueprint('documented_api', __name__)

api_extension = Api(
    blueprint,
    title='Flask RESTplus Demo',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation',
    doc='/'
)

api_extension.add_namespace(restaurants_ns)
