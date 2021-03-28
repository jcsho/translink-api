import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS']);
db = SQLAlchemy(app)

from models import Stop, Bus

@app.route('/')
def hello():
    return "Hello World!"

print(os.environ['APP_SETTINGS'])
    
if __name__ == '__main__':
    app.run()