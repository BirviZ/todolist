from email.policy import default
from app import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, index=True)
    isComplete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        str = ''

        if len(self.body) > 20:
            str = self.body[:20]
            str += '...'
        else:
            str = self.body
        return str