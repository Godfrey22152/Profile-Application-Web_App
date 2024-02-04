from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from pymongo import MongoClient
from bson.objectid import ObjectId
import re
import os
import random

app = Flask(__name__)
app.secret_key = 'your secret key'

# MongoDB configuration
client = MongoClient('mongodb://my_mongodb:27017/')
db = client['ProfileApp']


@app.route('/')
@app.route('/landing')
def landing():
    images = ['image1.jpeg', 'image2.jpg', 'image3.png', 'image4.jpeg']
    random.shuffle(images)  # Shuffle the images

    return render_template('landing.html', images=images)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
        account = db.accounts.find_one({'username': username, 'password': password})

        if account:
            session['loggedin'] = True
            session['id'] = str(account['_id'])
            session['username'] = account['username']
            msg = 'Logged in successfully!'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Incorrect username / password!'

    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)

    # Add a flag to indicate whether to show the "Return Home" button on the login page
    show_return_home = request.args.get('show_return_home', False)

    return render_template('login.html', msg='Logged out successfully!', show_return_home=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        organisation = request.form['organisation']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        postalcode = request.form['postalcode']

        existing_account = db.accounts.find_one({'username': username})

        if existing_account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Name must contain only characters and numbers!'
        else:
            db.accounts.insert_one({
                'username': username,
                'password': password,
                'email': email,
                'organisation': organisation,
                'address': address,
                'city': city,
                'state': state,
                'country': country,
                'postalcode': postalcode
            })
            msg = 'You have successfully registered!'

    elif request.method == 'POST':
        msg = 'Please fill out the form!'

    return render_template('register.html', msg=msg)

@app.route("/index")
def index():

    if 'loggedin' in session:

        return render_template("index.html")

    return redirect(url_for('login'))

@app.route("/display")
def display():
    if 'loggedin' in session:
        account = db.accounts.find_one({'_id': ObjectId(session['id'])})
        return render_template("display.html", account=account)
    return redirect(url_for('login'))

@app.route("/update", methods=['GET', 'POST'])
def update():
    msg = ''
    if 'loggedin' in session:
        if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'address' in request.form and 'city' in request.form and 'country' in request.form and 'postalcode' in request.form and 'organisation' in request.form:
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            organisation = request.form['organisation']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            country = request.form['country']
            postalcode = request.form['postalcode']

            existing_account = db.accounts.find_one({'username': username, '_id': {'$ne': ObjectId(session['id'])}})

            if existing_account:
                msg = 'Account already exists!'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address!'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Name must contain only characters and numbers!'
            else:
                db.accounts.update_one(
                    {'_id': ObjectId(session['id'])},
                    {'$set': {
                        'username': username,
                        'password': password,
                        'email': email,
                        'organisation': organisation,
                        'address': address,
                        'city': city,
                        'state': state,
                        'country': country,
                        'postalcode': postalcode
                    }}
                )
                msg = 'You have successfully updated!'

        elif request.method == 'POST':
            msg = 'Please fill out the form!'

        return render_template("update.html", msg=msg)

    return redirect(url_for('login'))

# route for the application form
@app.route('/application', methods=['GET', 'POST'])
def application():
    msg = ''
    existing_application = db.application.find_one({'user_id': ObjectId(session['id'])})

    if existing_application:
        msg = 'ONLY ONE APPLICATION IS PERMITTED !!!'
    else:
        if request.method == 'POST':
            preferred_skill = request.form.get('preferred_skill')
            description = request.form.get('description')
            education_level = request.form.get('education_level')
            institution = request.form.get('institution')
            course = request.form.get('course')
            certificate = request.form.get('certificate')
            grade = request.form.get('grade')
            computer_skills_rating = request.form.get('computer_skills_rating')
            experience_years = request.form.get('experience_years')
            age = request.form.get('age')

            db.application.insert_one({
                'user_id': ObjectId(session['id']),
                'preferred_skill': preferred_skill,
                'description': description,
                'education_level': education_level,
                'institution': institution,
                'course': course,
                'certificate': certificate,
                'grade': grade,
                'computer_skills_rating': computer_skills_rating,
                'experience_years': experience_years,
                'age': age
            })

            msg = 'Application submitted successfully!'

    return render_template('application.html', msg=msg, existing_application=existing_application)

@app.route('/application_details')
def application_details():
    if 'loggedin' in session:
        application = db.application.find_one({'user_id': ObjectId(session['id'])})
        return render_template('app_details.html', application=application)


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
