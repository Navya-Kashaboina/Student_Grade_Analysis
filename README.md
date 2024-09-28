# Flask Machine Learning Student Project

## Overview
This project is a simple Flask web application that allows users to submit their information (name, age, and a short bio) through a form. The submitted data is saved to a text file. Additionally, the project includes functionality to generate a CSV file with student data and implement a machine learning model.

## Features
- Home Page: A welcome page that greets the user.
- Form Page: A form to collect user data (name, age, bio).
- Display Page: Displays the submitted user data.
- CSV Generation: Generates a CSV file with student data.
- Machine Learning: Trains a simple model and visualizes data.

## Requirements
- Python 3.x
- Flask
- pandas

## Setup Instructions
1. Clone this repository or download the files.
2. Navigate to the project directory.
3. Create a virtual environment:
4. Activate the virtual environment:
- For Windows PowerShell:
  ```
  .\venv\Scripts\Activate
  ```
5. Install the required packages:
6. Run the Flask application:
7. Open your browser and go to `http://127.0.0.1:5000/`.

## Notes
- Ensure that you have all necessary dependencies installed.
- Feel free to modify and extend the application as needed.
flask_ml_student_project/
│
├── templates/
│   ├── home.html        # Home page: Welcomes users to the application.
│   ├── form.html        # Form page: Allows users to enter their name, age, and a short bio.
│   └── display.html     # Display page: Shows the data submitted by users in a formatted way.
│
├── static/
│   └── style.css        # CSS styles: Defines the visual style of the web application.
│
├── app.py               # Main Flask application: Contains the core logic for routing, form handling, and rendering templates.
├── model_training.ipynb  # Jupyter Notebook: Includes code for training the machine learning model, generating visualizations, and saving the model as a .pkl file.
├── students.csv         # CSV file: Contains records of 100 students with their names, ages, and grades.
├── model.pkl            # Pickle file: Stores the trained machine learning model for later use in predictions.
├── users.txt            # Text file: Saves the data submitted through the user form, storing names, ages, and bios for future reference.
├── requirements.txt     # Required packages: Lists all necessary Python libraries and their versions needed to run the application.
└── README.md            # Project documentation: Provides an overview of the project, instructions on how to run the application, and any additional notes.



