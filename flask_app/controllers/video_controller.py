from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.video_model import Video

@app.route('/add_video', methods = ["POST"])
def add_video():
    data = {
        'video' : Video.shorten(request.form['video']),
        'notes' : request.form['notes'],
        'user_id' : request.form['user_id']
    }
    Video.save(data)
    return redirect(f"/thrower/{data['user_id']}")