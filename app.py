from flask import Flask

from config.custom_exception import handle_not_acceptable
from controller.restaurants_controller import restaurants_blueprint
from documented_endpoints import blueprint as documented_endpoint

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(restaurants_blueprint)
app.register_blueprint(documented_endpoint)

app.register_error_handler(406, handle_not_acceptable)

if __name__ == '__main__':
    app.run()
