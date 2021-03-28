from app import db
from geoalchemy2 import Geography

# migrations require modifications to import geoalchemy types
# http://codeomitted.com/flask-postgis-and-alembic-migration/

class Stop(db.Model):
    __tablename__ = 'stops'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    number = db.Column(db.Integer)
    location = db.Column(Geography(geometry_type='POINT', srid=4326))
    
    def __init__(self, name, number, location):
        self.name = name
        self.number = number
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
        
class Bus(db.Model):
    __tablename__ = 'buses'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicleId = db.Column(db.Integer)
    location = db.Column(Geography(geometry_type='POINT', srid=4326))
    
    def __init__(self, vehicleId, location):
        self.vehicleId = vehicleId
        self.location = location
        
    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    