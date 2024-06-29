from flask import Flask, request, jsonify, make_response
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure upload folder (replace with your desired location)
UPLOAD_FOLDER = './temp'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'image' not in request.files:
            return make_response(jsonify({'error': 'No file part'}), 400)

        image_file = request.files['image']

        # Check if the file has a filename
        if image_file.filename == '':
            return make_response(jsonify({'error': 'No selected file'}), 400)

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)

            try:
                image_file.save(image_path)
                return jsonify({'message': f'Image uploaded successfully! (Filename: {filename})'})
            except Exception as e:
                return make_response(jsonify({'error': f'Failed to save image: {str(e)}'}), 500)

        else:
            return make_response(jsonify({'error': 'Unsupported file format'}), 400)

    else:
        return make_response(jsonify({'error': 'Method Not Allowed'}), 405)


if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))