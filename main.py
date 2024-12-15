from flask import Flask, render_template, request, session, redirect, url_for
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MySQL Configuration
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Nishu@1979',
    database='mindsyncplus_db'
)
cursor = db.cursor()

# Dictionary to map model names to file paths
MODEL_PATHS = {
    'model1': r"static\models\ASC_saved.h5",
    'model2': r"static\models\Inception_V3_saved.h5",
    'model3': r"static\models\VGG19_saved.h5",
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cog')
def cog():
    if session.get('logged_in'):
        return render_template('cog.html')
    else:
        session['previous_page'] = url_for('cog')
        return redirect(url_for('login'))

@app.route('/contact')
def contact():
    if session.get('logged_in'):
        return render_template('contact.html')
    else:
        session['previous_page'] = url_for('contact')
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        login_type = request.form.get('loginType')  # Gets login type from dropdown
        identifier = request.form.get('identifier')  # Identifier could be username, email, or phone
        password = request.form.get('password')  # Password field

        # Determine which column to use in the database based on login type
        if login_type == 'username':
            column_name = 'username'
        elif login_type == 'email':
            column_name = 'email'
        elif login_type == 'phone':
            column_name = 'phone_number'

        # Check credentials in the database
        query = f"SELECT * FROM users WHERE {column_name} = %s AND password = %s"
        cursor.execute(query, (identifier, password))
        user = cursor.fetchone()

        if user:
            # Set session variables to indicate user is logged in
            session['logged_in'] = True
            session['user_id'] = user[0]  # Assuming first column is user ID

            return redirect(url_for('index'))
        else:
            # If login fails, show an error message
            error = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=error)

    # If GET request, render the login page
    return render_template('login.html', error=None)

@app.route('/predict_image_file', methods=['POST'])
def predict_image_file():
    if request.method == 'POST':
        selected_model = request.form.get('model')
        model_path = MODEL_PATHS.get(selected_model)

        if model_path is None:
            return render_template('error.html', message='Invalid model selection')

        try:
            model = load_model(model_path)
        except Exception as e:
            return render_template('error.html', message=f'Error loading model: {e}')

        img_file = request.files['file']
        img = Image.open(img_file)
        img = img.resize((120, 120))
        img = img.convert("L")
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array.astype('float32') / 255.0

        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        confidence = predictions[0][predicted_class]

        class_labels = ["NonDemented", "MildDemented", "ModerateDemented", "VeryMildDemented"]
        predicted_label = class_labels[predicted_class]

        if predicted_label == 'VeryMildDemented':
            return render_template('vmild_dem.html')
        elif predicted_label == 'MildDemented':
            return render_template('mild_dem.html')
        elif predicted_label == 'ModerateDemented':
            return render_template('mod_dem.html')
        elif predicted_label == 'NonDemented':
            return render_template('non_dem.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')

        if not (username and email and phone and password):
            return render_template('signup.html', error='All fields are required.')

        try:
            insert_query = "INSERT INTO users (email, password, phone_number, username) VALUES (%s, %s, %s, %s)"
            user_data = (email, password, phone, username)
            cursor.execute(insert_query, user_data)
            db.commit()

            session['logged_in'] = True

            previous_page = session.get('previous_page')
            if previous_page in ['/cog', '/contact']:
                return redirect(previous_page)
            else:
                return redirect(url_for('index'))

        except mysql.connector.Error as err:
            return render_template('signup.html', error=f'Database error: {err}')

    return render_template('signup.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)
