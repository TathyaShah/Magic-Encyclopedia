from flask import Flask, render_template, request, url_for, redirect, session
from flask_pymongo import PyMongo
import bcrypt
from bson import ObjectId

app = Flask(__name__, template_folder='template')
app.secret_key='magic_encyclopedia'
mongo1 = PyMongo(app, uri="mongodb://localhost:27017/users")
mongo2 = PyMongo(app, uri="mongodb://localhost:27017/objects")

@app.route('/')
def index():
    username = session.get('username')

    if username:
        user_data = mongo1.db.details.find_one({'username': username})
        return render_template('index.html', user_data=user_data, logged_in=True)
    else:
        return render_template('index.html', logged_in=False)

@app.route('/alphabets')
def display_data():
    details = list(mongo2.db.info.find())
    username = session.get('username')
    grouped_details = {}
    if username:
        for item in details:
            category = item['category']
            first_letter = item['heading'][0].upper()
            if first_letter not in grouped_details:
                grouped_details[first_letter] = []
            grouped_details[first_letter].append(item)
        grouped_details = dict(sorted(grouped_details.items()))
        return render_template('alphabets.html', username=username, grouped_details=grouped_details)
    else:
        return "Please log in to access this route."

@app.route('/add_to_favorites/<object_id>', methods=['POST'])
def add_to_favorites(object_id):
    if request.method == 'POST':
        object_id = ObjectId(object_id)
        username = session.get('username')
        is_favorite = mongo1.db.info.find_one({'favorites': object_id})
        if is_favorite:
            mongo1.db.details.update_one({'username': username}, {'$pull': {'favorites': object_id}})
        else:
            mongo1.db.details.update_one({'username': username}, {'$push': {'favorites': object_id}})
        return redirect(url_for('display_data'))

@app.route('/remove_from_favorites/<object_id>', methods=['POST'])
def remove_from_favorites(object_id):
    username = session.get('username')
    object_id = ObjectId(object_id)

    if username:
        mongo1.db.details.update_one({'username': username}, {'$pull': {'favorites': object_id}})
        return redirect(url_for('favorites'))
    else:
        return "Please log in to access this route."


@app.route('/favorites', methods=['GET'])
def favorites():
    username = session.get('username')

    if username:
        user_data = mongo1.db.details.find_one({'username': username})
        favorite_ids = user_data.get('favorites', [])
        favorites_data = list(mongo2.db.info.find({'_id': {'$in': favorite_ids}}))

        return render_template('favorites.html', username=username, favorites_data=favorites_data)
    else:
        return "Please log in to access this route."

@app.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = mongo1.db.details.find_one({'username': username, 'password': password})
        if user:
            session['username'] = username
            return redirect(url_for('index', username=username))
        else:
            login_message_error="Invalid details, please signup if new user"
        return render_template('login.html',login_message_error=login_message_error)
    # return render_template('login.html')
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if len(password) < 6:
            signup_message_error='Password must be at least 6 characters long'
            return render_template('signup.html',signup_message_error=signup_message_error)
        
        existing_user = mongo1.db.details.find_one({'username': username})

        if existing_user:
            existinguser="User already exists, please login"
            return render_template('signup.html',existinguser=existinguser)
        else:
            mongo1.db.details.insert_one({'username': username, 'password': password})
            account_created="Account created. Now please log in again"
            return render_template('signup.html',account_created=account_created)         
    return redirect('/')



if __name__== '__main__':
    app.run(debug=True)