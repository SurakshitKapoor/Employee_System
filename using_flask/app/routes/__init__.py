
from flask import Flask
from app.database import init_db
from app.routes.employees import employees_bp

def create_app():
    app = Flask(__name__)

    init_db()
    app.register_blueprint(employees_bp)

    return app
