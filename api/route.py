from flask import Blueprint, jsonify, request
from models import Route, Stop
from app import db

route_controller = Blueprint('route_controller', __name__)

@route_controller.route('/api/route', methods=['GET'])
def get_routes():

    routes = None
    if request.is_json:
      filters = request.json.get('filters')
      if 'stopNo' in filters:
        routes = Stop.query.filter_by(number=filters['stopNo']).join(Route)
    else:
      routes = route.get_all()

    return jsonify({'routees': list(map(lambda route: route.serialize(), routes))})

@route_controller.route('/api/route/<id>', methods=['GET'])
def get_route(id):
    return jsonify(route.query.get(id).serialize())

@route_controller.route('/api/route', methods=['POST'])
def create_route():
    result = ''
    error = ''
    try:
        route = Route(
            request.json['routeId'],
            request.json['busId'],
            request.json['stopId']
        )
        route.save()
        print('Added route: ', route)
        result = 'Added route: {0}'.format(route.serialize())
    except Exception as err:
        print('Unexpected error:', err)
        error = 'Error: {0}'.format(err)
    
    return jsonify({'result': result, 'error': error})

@route_controller.route('/api/route/<id>', methods=['PUT'])
def update_route(id):
    route = route.query.get(id)
    route.route_id = request.json['routeId']
    route.bus_id = request.json['busId']
    route.stop_id = request.json['stopId']
    db.session.commit()
    return jsonify({'route': route.serialize()})

@route_controller.route('/api/route/<id>', methods=['DELETE'])
def delete_route(id):
    result = False
    try:
        route = route.query.get(id)
        route.delete()
        result = True
    except Exception as err:
        print(err)
    
    return jsonify({'result': result})