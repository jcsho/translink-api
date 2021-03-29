from app import db
from sqlalchemy.orm import relationship, backref
from .bus import Bus
from .stop import Stop

class Route(db.Model):
  __tablename__ = 'routes'

  id = db.Column(db.Integer, primary_key=True)
  route_id = db.Column(db.Integer)
  bus_id = db.Column(db.Integer, db.ForeignKey('buses.id'))
  stop_id = db.Column(db.Integer, db.ForeignKey('stops.id'))

  bus = relationship(Bus, backref=backref("routes"))
  stop = relationship(Stop, backref=backref("routes"))
