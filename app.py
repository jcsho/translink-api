import os, sys
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS']);
db = SQLAlchemy(app)

from models import Stop, Bus

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/bus', methods=['GET'])
def get_buses():
    return jsonify({'buses': list(map(lambda bus: bus.serialize(), Bus.query.all()))})

@app.route('/api/bus/<id>', methods=['GET'])
def get_bus(id):
    return jsonify(Bus.query.get(id).serialize())

@app.route('/api/bus', methods=['POST'])
def create_bus():
    result = ''
    error = ''
    try:
        bus = Bus(
            request.json["vehicleId"],
            'POINT({0} {1})'.format(request.json["longitude"], request.json["latitude"])
        )
        db.session.add(bus)
        db.session.commit()
        print("Added bus: ", bus)
        result = "Added bus: {0}".format(bus.serialize)
    except err:
        print("Unexpected error:", err)
        error = "Error: {0}".format(err)
    
    return jsonify({"result": result, "error": error})

@app.route('/api/bus/<id>', methods=['PUT'])
def update_bus(id):
    bus = Bus.query.get(id)
    bus.vehicleId = request.json.get('vehicleId', bus.vehicleId)
    long = request.json.get('longitude', bus.longitude())
    lat = request.json.get('latitude', bus.latitude())
    bus.location = 'POINT({0} {1})'.format(long, lat)
    db.session.commit()
    return jsonify({"Bus": bus.serialize()})

@app.route('/api/bus/<id>', methods=['DELETE'])
def delete_bus(id):
    result = False
    try:
        db.session.delete(Bus.query.get(id))
        db.session.commit()
        result = True
    except err:
        print(err)
    
    return jsonify({"result": result})

print(os.environ['APP_SETTINGS'])
    
if __name__ == '__main__':
    app.run()