# Deep-Fake-Detection-Tool
Deep Fake Detection Tool
Overview
Welcome to the Deep Fake Detection Tool! This project aims to provide a robust and user-friendly web application for detecting deepfake images. Leveraging the power of deep learning, our tool helps users identify whether an image is real or a deepfake.

Features
User Authentication: Secure login and signup pages to manage user access.
Deep Fake Detection: Upload an image to determine whether it is real or a deepfake using our trained model.
Face Recognition Tool: An additional tool to recognize faces in images.
History Logging: Keep track of all scans performed with timestamps and results.
Intuitive UI: A clean and modern interface for seamless user experience.
Technology Stack
Backend: Flask framework
Frontend: HTML, CSS, JavaScript
Database: SQLite for storing user credentials and scan history
Model: TensorFlow/Keras for deepfake detection
Getting Started
Prerequisites
Python 3.x
Flask
TensorFlow/Keras
OpenCV
SQLite
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/deepfake-detection-tool.git
cd deepfake-detection-tool
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Set up the database:

bash
Copy code
python setup_db.py
Run the Flask application:

bash
Copy code
flask run
Open your web browser and navigate to http://127.0.0.1:5000/.

Usage
Sign Up: Create a new account using the signup page.
Login: Log in using your credentials.
Deep Fake Detection: Navigate to the Deep Fake Detection Tool, upload an image, and click "Scan" to get the prediction.
History: View your scan history by clicking the "History" button.
Project Structure
plaintext
Copy code
deepfake-detection-tool/
│
├── app.py                 # Main application script
├── dfscanner.py           # Deep fake detection logic
├── setup_db.py            # Script to initialize the database
├── static/
│   ├── dfstyle.css        # CSS for the deep fake detection page
│   ├── index_style.css    # CSS for the index page
│   ├── style.css          # CSS for the login and signup pages
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Index page
│   ├── login.html         # Login page
│   ├── signup.html        # Signup page
│   ├── dfscanner.html     # Deep fake detection page
│   ├── history.html       # History page
└── README.md              # Project introduction and setup instructions
Contributing
We welcome contributions! Please fork the repository and submit a pull request for any features, bug fixes, or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thank you to the contributors of TensorFlow, Keras, Flask, and OpenCV for providing the tools and libraries that make this project possible.
