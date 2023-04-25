from flask import Flask, render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)


@app.route('/')
def home():
    return render_template("login.html")


@app.route('/sign_up', methods = ['POST'])
def sign_up():
    if not User.validate_sign_up(request.form):
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['pass'])
    # print(pw_hash)
    data = {
        'first_name':request.form['fname'],
        'last_name':request.form['lname'],
        'email':request.form['email'],
        'password':pw_hash,
        'position':request.form['position']
    }
    user_id = User.save(data)
    session['user_id'] = user_id

    return redirect('/dashboard')


@app.route('/login', methods = ['POST'])
def login():
    logged_in_user = User.validate_login(request.form)
    if logged_in_user:
        session['user_id'] = logged_in_user.id
        session['user_pos'] = logged_in_user.position
        return redirect("/dashboard")
    else:
        return redirect('/')


@app.route('/add_thrower', methods = ['POST'])
def add_thrower():
    User.add_thrower(request.form, suser = User.get_one(session['user_id']))
    return redirect('/dashboard')


@app.route('/dashboard')
def dash():
    suser = User.get_one(session['user_id'])
    if suser.position != 0:
        return redirect(f'/thrower/{suser.id}')
    users = User.get_all_throwers(suser)
    return render_template('coach_dash.html', suser = suser, users = users )

@app.route('/thrower/<int:id>')
def thrower(id):
    user = User.get_one(id)
    return render_template('thrower.html', user = user, suser = User.get_one(session['user_id']))



@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')