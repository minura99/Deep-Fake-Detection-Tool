# Deep-Fake-Detection-Tool
Deep Fake Detection Tool
## Overview
Welcome to the Deep Fake Detection Tool! This project aims to provide a robust and user-friendly web application for detecting deepfake images. Leveraging the power of deep learning, our tool helps users identify whether an image is real or a deepfake.

## Features
User Authentication: Secure login and signup pages to manage user access.
Deep Fake Detection: Upload an image to determine whether it is real or a deepfake using our trained model.
Face Recognition Tool: An additional tool to recognize faces in images.
History Logging: Keep track of all scans performed with timestamps and results.
Intuitive UI: A clean and modern interface for seamless user experience.
## Technology Stack
##### Backend: Flask framework
##### Frontend: HTML, CSS, JavaScript
##### Database: SQLite for storing user credentials and scan history
##### Model: TensorFlow/Keras for deepfake detection
## Getting Started
1. Clone the repository:
   ```bash
   $ git clone https://github.com/minura99/deep-fake-detection-tool.git
2. ```bash
   cd deepfake-detection-tool
3. Create and activate a virtual environment:
   ```bash
   $ python -m venv venv
   $ venv\Scripts\activate  # On Windows Users
   $ source venv/bin/activate # On Linux Users
4. Install the required packages:
   ```bash
   $  pip install -r requirements.txt
## Training the Model
1. Collect the Dataset
2. Train the model using dataset
    ```bash
   $ python train_model.py "Dataset Image path"  "Training model Directory"
## Usage
1. Run the Flask application:
    ```bash
    $ flask run
    # Open your web browser and navigate to http://127.0.0.1:5000/.
2. Sign Up: Click the signup and Create a new account
![Example Image 1](images/logscreen.png)
3. Login: Log in using your credentials.
4  Deep Fake Detection: Navigate to the Deep Fake Detection Tool, upload an image, and click "Scan" to get the prediction.
5. History: View your scan history by clicking the "History" button.

   
## Project Structure
1. deepfake-detection-tool/
   ```bash
   
   │
   ├── app.py # Main application script
   ├── dfscanner.py # Deep fake detection logic
   ├── setup_db.py # Script to initialize the database
   ├── static/
   │ ├── dfstyle.css # CSS for the deep fake detection page
   │ ├── index_style.css # CSS for the index page
   │ ├── style.css # CSS for the login and signup pages
   ├── templates/
   │ ├── base.html # Base template
   │ ├── index.html # Index page
   │ ├── login.html # Login page
   │ ├── signup.html # Signup page
   │ ├── dfscanner.html # Deep fake detection page
   │ ├── history.html # History page
   └── requirements.txt
   └── README.md # Project introduction and setup instructions

## Contributing
We welcome contributions! Please fork the repository and submit a pull request for any features, bug fixes, or improvements.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thank you to the contributors of TensorFlow, Keras, Flask, and OpenCV for providing the tools and libraries that make this project possible.
