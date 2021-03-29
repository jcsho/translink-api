import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS']);
db = SQLAlchemy(app)

from models import Stop, Bus
from api.bus import bus_controller
from api.stop import stop_controller

app.register_blueprint(bus_controller)
app.register_blueprint(stop_controller)

@app.route('/')
def hello():
    return "Hello World!"

print(os.environ['APP_SETTINGS'])
    
if __name__ == '__main__':
    app.run()