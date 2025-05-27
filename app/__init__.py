from flask import Flask
from flasgger import Swagger


# Initialize the Flask app
app = Flask(__name__)
app.config.from_object('app.config.Config')


# Configure Swagger
swagger = Swagger(app)


# Import routes (after 'app' is fully initialized)
from app.routes import auth_routes
from app.routes import scrape_route
