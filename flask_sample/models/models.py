from datetime import datetime
from flask_sample.database import db


class Info(db.Model):

  __tablename__ = 'infos'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255))
  subject = db.Column(db.String(255))
  affiliation = db.Column(db.String(255))
  email = db.Column(db.String(255))
  contents = db.Column(db.String(600))
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
  # updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

  def get_detail(self):
    return {'id': self.id, 'name': self.name, 'subject': self.subject, 'affiliation': self.affiliation,
            'email': self.email, 'contents': self.contents, 'created_at': self.created_at}

