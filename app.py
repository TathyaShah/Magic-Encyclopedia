from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__, template_folder='template')
app.secret_key='magic_encyclopedia'
mongo1 = PyMongo(app, uri="mongodb://localhost:27017/users")
mongo2 = PyMongo(app, uri="mongodb://localhost:27017/objects")

@app.route('/')
def index():
    # Check if the user is logged in by checking if the username is stored in the session
    username = session.get('username')

    if username:
        # If the user is logged in, render the personalized home page
        return redirect('/')
    return render_template('index.html')

@app.route('/alphabets')
def display_data():
    details = list(mongo2.db.info.find())

    # Group items based on the first letter of the heading
    grouped_details = {}
    for item in details:
        category=item['category']
        first_letter = item['heading'][0].upper()
        if first_letter not in grouped_details:
            grouped_details[first_letter] = []
        grouped_details[first_letter].append(item)
    grouped_details = dict(sorted(grouped_details.items()))
    return render_template('alphabets.html', grouped_details=grouped_details)

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the user credentials are valid in the MongoDB database
        user = mongo1.db.details.find_one({'username': username, 'password': password})

        if user:
            # If the user is found, redirect to the home page
            return render_template('index.html', username=username)
        else:
            # If the user is not found, display "Invalid details" message
            login_message_error="Invalid details, please signup if new user"
            return render_template('login.html',login_message_error=login_message_error)
    return render_template('login.html')

@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the password meets the minimum length requirement
        if len(password) < 6:
            signup_message_error='Password must be at least 6 characters long'
            return render_template('signup.html',signup_message_error=signup_message_error)
        
        # Check if the username already exists in the database
        existing_user = mongo1.db.details.find_one({'username': username})

        if existing_user:
            # If the username is already registered, redirect to login with a message
            existing_user="User already exists, please login"
            return render_template('signup.html',existing_user=existing_user)
        else:
            # If the username is not registered, create a new account
            mongo1.db.details.insert_one({'username': username, 'password': password})
            account_created="Account created. Now please log in again"
            return render_template('signup.html',account_created=account_created)         
    return redirect('/')



if __name__== '__main__':
    app.run(debug=True)