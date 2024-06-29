import os
from flask import current_app
from werkzeug.utils import secure_filename

# Path where images will be saved
UPLOAD_FOLDER = 'static/uploads'

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def save_image(image_file):
    """Save the uploaded image and return the filename."""
    filename = secure_filename(image_file.filename)
    filepath = os.path.join(current_app.root_path, UPLOAD_FOLDER, filename)
    image_file.save(filepath)
    return filename
