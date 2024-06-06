from flask import Flask
from flask_jwt_extended import JWTManager

from .config import config
from .database import db, migrate
from app.main.routes import task_routes
from app.main.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Cambia esto por una clave segura
    
    jwt = JWTManager(app)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(task_routes)
    app.register_blueprint(auth_bp)

    return app