from app import db

class Image(db.Model):
    __tablename__ = "image_description"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120), unique=True, nullable=False)
    filepath = db.Column(db.String(120))
    upload_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"Image('{self.filename}', '{self.upload_time}')"

class ImageInformation(db.Model):
    __tablename__ = 'image_information'

    id = db.Column(db.Integer, primary_key=True)
    worker_details_id = db.Column(db.Integer, nullable=False)
    body_part_name = db.Column(db.String(255), nullable=False)
    kp_x = db.Column(db.Float, nullable=True)
    kp_y = db.Column(db.Float, nullable=True)
    image_path = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(50), nullable=True)
    safety_equipment = db.Column(db.String(100), nullable=True)
    safety_equipment_description = db.Column(db.Text, nullable=True)
    posture_risk_level = db.Column(db.String(20), nullable=True)
    back_angle = db.Column(db.Float, nullable=True)
    neck_angle = db.Column(db.Float, nullable=True)
    arm_elevation = db.Column(db.String(50), nullable=True)
    leg_position = db.Column(db.String(50), nullable=True)
    knee_angle = db.Column(db.Float, nullable=True)
    lifting_status = db.Column(db.Boolean, nullable=True)
    lifting_technique = db.Column(db.String(50), nullable=True)
    lifting_height = db.Column(db.String(50), nullable=True)
    repetitive_motion = db.Column(db.Boolean, nullable=True)
    repetitive_motion_type = db.Column(db.String(50), nullable=True)
    tool_usage = db.Column(db.Boolean, nullable=True)
    tool_grip_ergonomics = db.Column(db.String(50), nullable=True)
    work_height = db.Column(db.String(50), nullable=True)
    balance_risk = db.Column(db.String(20), nullable=True)
    ppe_compliance = db.Column(db.Boolean, nullable=True)
    ppe_missing_items = db.Column(db.String(255), nullable=True)
    environmental_hazards = db.Column(db.Text, nullable=True)
    fatigue_indicators = db.Column(db.String(20), nullable=True)
    ergonomic_risk_score = db.Column(db.Float, nullable=True)
    recommended_interventions = db.Column(db.Text, nullable=True)
    time_in_current_posture = db.Column(db.Interval, nullable=True)
    cumulative_strain_index = db.Column(db.Float, nullable=True)
    task_repetition_count = db.Column(db.Integer, nullable=True)
    energy_expenditure_estimate = db.Column(db.Float, nullable=True)