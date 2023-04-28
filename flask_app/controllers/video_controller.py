from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.video_model import Video
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'flask_app\\static\\files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg', 'gif', 'mov', 'mp4', 'avi' }

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_video', methods = ["POST"])
def add_video():
    # check if the post request has a file part
    if 'video' not in request.files:
        flash('No file part')
        return redirect(f'/thrower/{request.form["user_id"]}')

    # if file part exists in form, save to variable
    file = request.files['video']

    # if the user does not select a file, browser submits an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(f'/thrower/{request.form["user_id"]}')

    # if valid file submitted, save into local folder (does *NOT* save in database!)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # saves the image into the static/img folder
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # saves img filename in SQL db for reference
        data = {
            'filename': filename,
            'notes' : request.form['notes'],
            'user_id' : request.form['user_id']
        }
        Video.save(data)
    return redirect(f"/thrower/{data['user_id']}")