import os
from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, send_from_directory
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import UploadForm
from app.models import Image
from app.vision_model import load_model, process_image

model = load_model()

@app.route('/')
@app.route('/home')
def home():
    form = UploadForm()
    return render_template('home.html', form=form)

@app.route('/upload', methods=['POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        upload_path = os.path.join(app.root_path, 'static/uploads', filename)
        image_file.save(upload_path)
        image = Image(filename=filename, upload_time=datetime.utcnow())
        db.session.add(image)
        db.session.commit()
        output_path = process_image(upload_path, model)
        return redirect(url_for('result', filename=filename))
    return render_template('home.html', form=form)

@app.route('/result/<filename>')
def result(filename):
    return render_template('result.html', filename=filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/uploads'), filename)

@app.route('/outputs/<filename>')
def output_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'static/outputs'), filename)
