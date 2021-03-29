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

  def __init__(self, route_id, bus_id, stop_id):
    self.route_id = route_id
    self.bus_id = bus_id
    self.stop_id = stop_id

    @staticmethod
    def get_all():
      return Route.query.all()

    def save(self):
      db.session.add(self)
      db.session.commit()

    def delete(self):
      db.session.delete(self)
      db.session.commit()