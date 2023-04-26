from flask import Flask, render_template, redirect, request, session
from flask_app import app
from flask_app.models.mark_model import Mark

@app.route('/add_mark', methods = ["POST"])
def add_mark():
    data = {
        'distance' : request.form['distance'],
        'date' : request.form['date'],
        'type' : request.form['event'],
        'user_id' : request.form['user_id']
    }
    Mark.save(data)
    return redirect(f"/thrower/{data['user_id']}")