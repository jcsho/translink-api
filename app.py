import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS']);
db = SQLAlchemy(app)

from api import *

app.register_blueprint(bus_controller)
app.register_blueprint(stop_controller)
app.register_blueprint(route_controller)

print(os.environ['APP_SETTINGS'])
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')