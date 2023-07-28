import os
from dotenv import load_dotenv
from oauth import get_access_token
import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient
from models import user, search_icd_code, prescription, medication, medical_record, icd_code, appointment
from faker import Faker

# Load environment variables from .env file
load_dotenv()

# Access the secret session variables 
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

app = Flask(__name__)
fake = Faker()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:5001")
db = client["test"]

# Define Routes and Handlers
@app.route('/testPoint')
def testPoint():
    # integrate code to access token and make API requests
    access_token = get_access_token()
    api_url = "https://id.who.int/icd/entity"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Accept-Language": "en",
        "API-Version": "v2",
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        content = response.json()
        return jsonify(content)  # return json response
    else:
        return f"Request failed: {response.status_code}", 500  # return error message

# Return a welcome message when accessing the root URL
@app.route('/')
def home():
    return "Welcome to World Health Organization Care App!"

# Error handler for Bad Request (HTTP 400)
@app.errorhandler(400)
def handle_bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# run Flask App
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)