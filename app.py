from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__, template_folder='template')
app.secret_key='magic_encyclopedia'
app.config["MONGO_URI"] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)

@app.route('/')
def index():
    # Check if the user is logged in by checking if the username is stored in the session
    username = session.get('username')

    if username:
        # If the user is logged in, render the personalized home page
        return redirect('/')
    return render_template('index.html')
def redirect_after_2_seconds():
    time.sleep(2)
    return redirect(url_for("index"))

@app.route('/alphabets')
def alphabets():
    return render_template('alphabets.html')

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the user credentials are valid in the MongoDB database
        user = mongo.db.details.find_one({'username': username, 'password': password})

        if user:
            # If the user is found, redirect to the home page
            return render_template('index.html', username=username)
        else:
            # If the user is not found, display "Invalid details" message
            return f"Invalid details, please signup if new user"
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
            return f'Password must be at least 6 characters long'
            return redirect('/signup')
        
        # Check if the username already exists in the database
        existing_user = mongo.db.details.find_one({'username': username})

        if existing_user:
            # If the username is already registered, redirect to login with a message
            return "User already exists, please login"
        else:
            # If the username is not registered, create a new account
            mongo.db.details.insert_one({'username': username, 'password': password})
            return "Account created. Now please log in again"
    return redirect('/')


if __name__== '__main__':
    app.run(debug=True)