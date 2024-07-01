from langchain.output_parsers import ResponseSchema

# Define the response schemas



response_schemas = [
    ResponseSchema(name="body_parts", description="list of body parts of the worker that are being used for the work."),
    ResponseSchema(name="worker_present", description="Whether a worker is visible in the image (true/false)"),
    ResponseSchema(name="worker_count", description="Number of workers visible in the image"),
    ResponseSchema(name="ppe_worn", description="List of PPE items worn by the worker(s)"),
    ResponseSchema(name="visible_tools", description="List of tools visible in the worker's hands or nearby"),
    ResponseSchema(name="environment_type", description="Type of construction environment shown"),
    ResponseSchema(name="back_position", description="Worker's back position (e.g., straight, bent, twisted)"),
    ResponseSchema(name="neck_position", description="Worker's neck position (e.g., neutral, flexed, extended, lateral)"),
    ResponseSchema(name="arm_position", description="Worker's arm position (e.g., below_shoulder, at_shoulder, above_shoulder)"),
    ResponseSchema(name="leg_position", description="Worker's leg position (e.g., standing, kneeling, squatting)"),
    ResponseSchema(name="lifting_status", description="Whether the worker is currently lifting an object (true/false)"),
    ResponseSchema(name="repetitive_motion", description="Whether the worker is performing repetitive motions (true/false)"),
    ResponseSchema(name="work_height", description="Height at which primary work is being performed"),
    ResponseSchema(name="balance_status", description="Worker's balance status (e.g., stable, unstable)"),
    ResponseSchema(name="work_surface", description="Type of surface the worker is standing on"),
    ResponseSchema(name="ergonomic_risk_level", description="Estimated overall ergonomic risk level (low, medium, high)"),
    ResponseSchema(name="fatigue_indicators", description="Presence of visible fatigue indicators (true/false)"),
    ResponseSchema(name="cumulative_risk_score", description="Estimated cumulative risk score on a scale of 1-10"),
    ResponseSchema(name="max_strain_in_part", description="which body part of the worker might have most strain"),

]
