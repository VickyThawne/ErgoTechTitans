from app import app, db
from app.forms import UploadForm
from app.models import Image
# from app.vision_model import load_model, process_image
from app.utils import save_image

# model = load_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        upload_path = os.path.join(app.root_path, 'static/uploads', filename)
        image_file.save(upload_path)
        image = Image(filename=filename, filepath=upload_path, upload_time=datetime.utcnow())
        db.session.add(image)
        db.session.commit()
        return redirect(url_for('result', filename=filename))
    return render_template('home.html', form=form)

@app.route('/upload', methods=['POST'])
	@@ -23,10 +32,10 @@ def upload():
        filename = secure_filename(image_file.filename)
        upload_path = os.path.join(app.root_path, 'static/uploads', filename)
        image_file.save(upload_path)
        image = Image(filename=filename, filepath=upload_path, upload_time=datetime.utcnow())
        db.session.add(image)
        db.session.commit()
        output_path = process_image(upload_path)
        return redirect(url_for('result', filename=filename))
    return render_template('home.html', form=form)