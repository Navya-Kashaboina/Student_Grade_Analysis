from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Load machine learning model
model = None
if os.path.exists('model.pkl'):
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# Form page
@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        bio = request.form['bio']
        
        # Save to a text file
        with open('users.txt', 'a') as file:
            file.write(f"{name}, {age}, {bio}\n")
        
        return "Form submitted successfully!"
    return render_template('form.html')

# Display submitted users
@app.route('/display')
def display():
    users = []
    with open('users.txt', 'r') as file:
        for line in file:
            name, age, bio = line.strip().split(", ")
            users.append({"name": name, "age": age, "bio": bio})
    return render_template('display.html', users=users)

# API to return users data
@app.route('/api/users', methods=['GET'])
def get_users():
    users = []
    with open('users.txt', 'r') as file:
        for line in file:
            name, age, bio = line.strip().split(", ")
            users.append({"name": name, "age": age, "bio": bio})
    return jsonify(users)

# Prediction (Optional example using the ML model)
@app.route('/predict', methods=['POST'])
def predict():
    age = request.json['age']
    prediction = model.predict([[age]]) if model else None
    return jsonify({"predicted_grade": prediction[0] if prediction is not None else "No model available"})

if __name__ == '__main__':
    app.run(debug=True)
