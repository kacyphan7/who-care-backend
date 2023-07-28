from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:5001")
db = client["test"]

# Define Routes and Handlers
@app.route('/')
def home():
    return "Welcome to World Health Organization Care App!"

# run Flask App
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)