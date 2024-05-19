from flask import Flask, render_template, request, redirect, session
from flask import jsonify
from dfscanner import load_trained_model, predict_deepfake
import sqlite3
import os
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

UPLOAD_FOLDER = 'uploads'
LOG_FILE_PATH = 'logs/scan_log.txt'

model = load_trained_model()
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['username'] = username
            return redirect('/')
        else:
            return render_template('error.html', error='Invalid username or password')
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('db/database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return redirect('/login')
    return render_template('signup.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect('/login')

# Route for deep fake detection tool
@app.route('/dfscanner', methods=['GET', 'POST'])
def deepfake_detection():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        image_file = request.files['image']
        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_path)

        prediction_result = predict_deepfake(model, image_path)

        # Log the result
        with open(LOG_FILE_PATH, 'a') as log_file:
            log_file.write(f"{datetime.datetime.now()} - Image: {image_path} - Prediction: {prediction_result}\n")

        return render_template('dfscanner.html', prediction=prediction_result)

    return render_template('dfscanner.html')


@app.route('/face_recognition')
def face_recognition():
    # Implement face recognition functionality
    return "Face Recognition Tool - Comming Soon........"

# Route for reading scan history
@app.route('/history', methods=['POST'])
def history():
    history = get_scan_history()
    return render_template('history.html', history=history)

# Function to get scan history
def get_scan_history():
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, 'r') as file:
            history = file.read()
        return history
    else:
        return "No scan history available"


if __name__ == '__main__':
    app.run(debug=True)
