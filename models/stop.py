from app import db
from geoalchemy2 import Geography
from geoalchemy2.functions import ST_X, ST_Y, ST_DWithin

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
        return '<Stop {}>'.format(self.name)

    def serialize(self):
        return {'id': self.id, 'name': self.name, 'stopNo': self.number, 'stopName': self.name, 'long': self.longitude(), 'lat': self.latitude()}
    
    def longitude(self):
        return db.session.scalar(ST_X(self.location))
    
    def latitude(self):
        return db.session.scalar(ST_Y(self.location))
        
    @staticmethod
    def get_all():
      return Stop.query.all()

    @staticmethod
    def get_within_area(longitude, latitude, radius=5):
      point = 'POINT({0} {1})'.format(longitude, latitude)
      return Stop.query.filter(ST_DWithin(Stop.location, point, radius))

    def save(self):
      db.session.add(self)
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()