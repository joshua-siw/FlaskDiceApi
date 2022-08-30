"""Flask Application"""

from prometheus_client import generate_latest
from flask import Flask, jsonify, session
from flask_session import Session

from src.api_spec import spec
from .blueprints.blueprint_dice import blueprint_dice
from .blueprints.blueprint_dicelist import blueprint_dicelist

# Initialisiere Flask App
app = Flask(__name__)
app.config.from_pyfile('config.py')
Session(app)

# Löscht die alten flask-session Daten
@app.before_first_request
def before_first_request():
    session.clear()


# Für Prometheus Metriken
@app.route('/metrics')
def metrics():
    return generate_latest()

# Registriere die Blueprints
app.register_blueprint(blueprint_dicelist, url_prefix="/api")
app.register_blueprint(blueprint_dice, url_prefix="/api")

