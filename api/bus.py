from flask import Blueprint, jsonify, request
from models import Bus
from app import db

bus_controller = Blueprint('bus_controller', __name__)

@bus_controller.route('/api/bus', methods=['GET'])
def get_buses():

    buses = None
    if request.is_json:
      filters = request.json.get('filters')
      if 'longitude' in filters or 'latitude' in filters:
        buses = Bus.get_within_area(
          filters['longitude'], 
          filters['latitude'],
          filters['radius']
        )
    else:
      buses = Bus.get_all()

    return jsonify({'buses': list(map(lambda bus: bus.serialize(), buses))})

@bus_controller.route('/api/bus/<id>', methods=['GET'])
def get_bus(id):
    return jsonify(Bus.query.get(id).serialize())

@bus_controller.route('/api/bus', methods=['POST'])
def create_bus():
    result = ''
    error = ''
    try:
        bus = Bus(
            request.json['vehicleId'],
            'POINT({0} {1})'.format(request.json['longitude'], request.json['latitude'])
        )
        bus.save()
        print('Added bus: ', bus)
        result = 'Added bus: {0}'.format(bus.serialize())
    except err:
        print('Unexpected error:', err)
        error = 'Error: {0}'.format(err)
    
    return jsonify({'result': result, 'error': error})

@bus_controller.route('/api/bus/<id>', methods=['PUT'])
def update_bus(id):
    bus = Bus.query.get(id)
    bus.vehicleId = request.json.get('vehicleId', bus.vehicleId)
    long = request.json.get('longitude', bus.longitude())
    lat = request.json.get('latitude', bus.latitude())
    bus.location = 'POINT({0} {1})'.format(long, lat)
    db.session.commit()
    return jsonify({'Bus': bus.serialize()})

@bus_controller.route('/api/bus/<id>', methods=['DELETE'])
def delete_bus(id):
    result = False
    try:
        bus = Bus.query.get(id)
        bus.delete()
        result = True
    except err:
        print(err)
    
    return jsonify({'result': result})