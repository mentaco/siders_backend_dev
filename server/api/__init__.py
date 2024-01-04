from flask import Flask
from .router import module_router
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(module_router, url_prefix='/api')

    return app

app = create_app()
