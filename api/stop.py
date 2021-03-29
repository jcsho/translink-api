from flask import Blueprint, jsonify, request
from models import Stop
from app import db

stop_controller = Blueprint('stop_controller', __name__)

@stop_controller.route('/api/stop', methods=['GET'])
def get_stops():
    stops = None
    if request.is_json:
      filters = request.json.get('filters')
      if 'longitude' in filters or 'latitude' in filters:
        stops = Stops.get_within_area(
          filters['longitude'], 
          filters['latitude'],
          filters['radius']
        )
    else:
      stops = Stops.get_all()
      
    return jsonify({'stops': list(map(lambda stop: stop.serialize(), stops))})

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
        stop.save()
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
        stop = Stop.query.get(id)
        stop.delete()
        result = True
    except err:
        print(err)
    
    return jsonify({'result': result})