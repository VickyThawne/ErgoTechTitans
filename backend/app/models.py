from app import db

class ImageDescription(db.Model):
    __tablename__ = "image_description"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)
    worker_details_id = db.Column(db.Integer, nullable=False)
    filepath = db.Column(db.String(120))
    upload_time = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(50), nullable=True)
    worker_present = db.Column(db.Boolean, nullable=False)
    worker_count = db.Column(db.Integer, nullable=False)
    ppe_worn = db.Column(db.String(50))
    visible_tools = db.Column(db.String(50))
    environment_type = db.Column(db.String(50))
    back_position = db.Column(db.String(50))
    neck_position = db.Column(db.String(50))
    arm_position = db.Column(db.String(50))
    leg_position = db.Column(db.String(50))
    lifting_status = db.Column(db.Boolean, nullable=False)
    repetitive_motion = db.Column(db.Boolean, nullable=False)
    work_height = db.Column(db.String(50))
    balance_status = db.Column(db.String(50))
    work_surface = db.Column(db.String(50))
    ergonomic_risk_level = db.Column(db.String(50))
    fatigue_indicators = db.Column(db.Boolean, nullable=False)
    cumulative_risk_score = db.Column(db.Integer, nullable=False)
    max_strain_in_part = db.Column(db.String(50))


    def __repr__(self):
        return f"Image('{self.filename}', '{self.upload_time}')"

class ImageInformation(db.Model):
    __tablename__ = 'image_information'

    id = db.Column(db.Integer, primary_key=True)
    worker_details_id = db.Column(db.Integer, nullable=False)
    filepath = db.Column(db.String(120))

    image_id = db.Column(db.Integer, nullable=True)
    kp_x = db.Column(db.Float, nullable=True)
    kp_y = db.Column(db.Float, nullable=True)
    distance= db.Column(db.Float, nullable=True)
    body_part_name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<ErgonomicAssessment {self.id}>'