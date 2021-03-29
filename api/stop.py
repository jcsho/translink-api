from flask import Blueprint, jsonify, request
from models import Stop
from app import db

stop_controller = Blueprint('stop_controller', __name__)

@stop_controller.route('/api/stop', methods=['GET'])
def get_stops():
  return jsonify({'stops': list(map(lambda stop: stop.serialize(), Stop.query.all()))})

@stop_controller.route('/api/stop/<id>', methods=['GET'])
def get_stop(id):
    return jsonify(Stop.query.get(id).serialize())

@stop_controller.route('/api/stop', methods=['POST'])
def create_stop():
    result = ''
    error = ''
    try:
        stop = Stop(
            request.json['name'],
            request.json['number'],
            'POINT({0} {1})'.format(request.json['longitude'], request.json['latitude'])
        )
        db.session.add(stop)
        db.session.commit()
        print('Added stop: ', stop)
        result = 'Added stop: {0}'.format(stop.serialize())
    except err:
        print('Unexpected error:', err)
        error = 'Error: {0}'.format(err)
    
    return jsonify({'result': result, 'error': error})

@stop_controller.route('/api/stop/<id>', methods=['PUT'])
def update_stop(id):
    stop = Stop.query.get(id)
    stop.name = request.json.get('name', stop.name)
    stop.number = request.json.get('number', stop.number)
    long = request.json.get('longitude', stop.longitude())
    lat = request.json.get('latitude', stop.latitude())
    stop.location = 'POINT({0} {1})'.format(long, lat)
    db.session.commit()
    return jsonify({'stop': stop.serialize()})

@stop_controller.route('/api/stop/<id>', methods=['DELETE'])
def delete_stop(id):
    result = False
    try:
        db.session.delete(Stop.query.get(id))
        db.session.commit()
        result = True
    except err:
        print(err)
    
    return jsonify({'result': result})