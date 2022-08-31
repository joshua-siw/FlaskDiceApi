from os import urandom
"""Flask Configuration"""

TESTING = True
DEBUG = True
FLASK_ENV = 'development'
# Generiere den Secret key für die flask_session
SECRET_KEY = urandom(12)
# Alternativ kann auch im cache gespeichert werden
SESSION_TYPE = 'filesystem'
# Wenn der Browser geschlossen wird ist die Sitzung beendet
SESSION_PERMANENT = False
