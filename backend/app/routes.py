import os
from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import UploadForm
from app.models import ImageDescription, ImageInformation

from langchain_app.script import analyze_construction_image, image_analysis_chain
# from app.vision_model import load_model, process_image
from app.utils import save_image
from random import choice
from sqlalchemy import func, not_
from sqlalchemy.orm import aliased

import json



from .extractor import process_image, take_diffrence

from langchain_app.response_schema import response_schemas
# model = load_model()
points = ["nose", "left_eye", "right_eye", "left_ear", "right_ear", "left_shoulder",
"right_shoulder", "left_elbow", "right_elbow", "left_wrist", "right_wrist", "left_hip", "right_hip",
"left_knee", "right_knee", "left_ankle", "right_ankle"]

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        upload_path = os.path.join(app.root_path, 'static/uploads', filename)
        image_file.save(upload_path)
        worker_detail_id = choice(["1249012497", "12349081280", "184098914"])[0]
        analysis_result = image_analysis_chain(upload_path)
        image = ImageDescription(
            filename=filename, 
            filepath=upload_path, 
            worker_details_id = worker_detail_id,

            upload_time=datetime.utcnow(),
            worker_present=analysis_result['worker_present'] == "true",
            worker_count=int(analysis_result['worker_count']),
            ppe_worn=analysis_result['ppe_worn'],
            visible_tools=analysis_result['visible_tools'],
            environment_type=analysis_result['environment_type'],
            back_position=analysis_result['back_position'],
            neck_position=analysis_result['neck_position'],
            arm_position=analysis_result['arm_position'],
            leg_position=analysis_result['leg_position'],
            lifting_status=analysis_result['lifting_status'] == "true",
            repetitive_motion=analysis_result['repetitive_motion'] == "true",
            work_height=analysis_result['work_height'],
            balance_status=analysis_result['balance_status'],
            work_surface=analysis_result['work_surface'],
            ergonomic_risk_level=analysis_result['ergonomic_risk_level'],
            fatigue_indicators=analysis_result['fatigue_indicators'] == "true",
            cumulative_risk_score=int(analysis_result['cumulative_risk_score']),
            max_strain_in_part=analysis_result['max_strain_in_part']
            )
        db.session.add(image)
        db.session.commit()

        data1 = process_image(upload_path)
        data2 = process_image("./base.jpg")

        diff = take_diffrence(data1, data2)
        for i in data1["keypoints"]:
            image_processing = ImageInformation(
                worker_details_id = worker_detail_id,
                filepath=upload_path,
                kp_x = i[0],
                kp_y = i[1],
                distance = diff[data1["keypoints"].index(i)],
                body_part_name = points[data1["keypoints"].index(i)],
            )
            db.session.add(image_processing)
            db.session.commit()

        return redirect(url_for('result', filename=filename))
    return render_template('home.html', form=form)

@app.route('/upload', methods=['POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        upload_path = os.path.join(app.root_path, 'static/uploads', filename)
        image_file.save(upload_path)
        image = Image(filename=filename, filepath=upload_path, upload_time=datetime.utcnow())
        db.session.add(image)
        db.session.commit()
        output_path = process_image(upload_path)
        return redirect(url_for('result', filename=filename))
    return render_template('home.html', form=form)

@app.route('/all_data', methods=['GET'])
def get_all_data():

    # Assuming 'db' is your SQLAlchemy database instance
    session = db.session

    # Build the query
    query = session.query(ImageDescription)

    # Execute the query and fetch all results
    results = query.all()

    # Convert results to list of dictionaries
    results_list = []
    for row in results:
        row_dict = {column.name: getattr(row, column.name) for column in ImageDescription.__table__.columns}
        results_list.append(row_dict)

    # Close the session
    session.close()
    print(results_list)
    return json.dumps(results_list, default=str)



@app.route('/table', methods=['GET'])
def get_table():
    session = db.session

    # Create an alias for the ImageInformation table
    t = aliased(ImageInformation)

    # Build the query
    query = (
        session.query(
            t.body_part_name,
            func.max(t.distance).label('distance')
        )
        .filter(t.worker_details_id == '1')
        .filter(~t.body_part_name.in_(['left_ear', 'right_ear', 'left_eye', 'right_eye', 'nose']))
        .group_by(t.body_part_name)
        .order_by(func.max(t.distance).desc())
    )

    labels = []
    distance = []

    results = query.all()


    for row in results:
        labels.append(row.body_part_name)
        distance.append(row.distance)

    result_dict = {
        "labels" : labels,
        "datasets" : distance
    }
    # Close the session
    session.close()
    print(result_dict)
    return jsonify(result_dict)
    # return 'Query executed successfully'
    # return render_template('home.html', form=form)    

@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/uploads'), filename)

@app.route('/outputs/<filename>')
def output_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/outputs'), filename)
