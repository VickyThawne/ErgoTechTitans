from app import db

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Image('{self.filename}', '{self.upload_time}')"
