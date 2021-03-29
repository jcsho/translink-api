from app import db
from geoalchemy2 import Geography
from geoalchemy2.functions import ST_X, ST_Y

# migrations require modifications to import geoalchemy types
# http://codeomitted.com/flask-postgis-and-alembic-migration/

class Bus(db.Model):
    __tablename__ = 'buses'
    
    id = db.Column(db.Integer, primary_key=True)
    vehicleId = db.Column(db.Integer)
    location = db.Column(Geography(geometry_type='POINT', srid=4326))
    
    def __init__(self, vehicleId, location):
        self.vehicleId = vehicleId
        self.location = location
        
    def __repr__(self):
        return '<Bus {}>'.format(self.vehicleId)

    def serialize(self):
        return {"id": self.id, "busId": self.vehicleId, "longitude": self.longitude(), "latitude": self.latitude()}

    def longitude(self):
        return db.session.scalar(ST_X(self.location))
    
    def latitude(self):
        return db.session.scalar(ST_Y(self.location))
    