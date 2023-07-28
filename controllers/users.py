import os
from dotenv import load_dotenv
from oauth import get_access_token
import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient
from models import user
from faker import Faker

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set up Faker
fake = Faker()

# user data for database 
users_data = []

# GET route all users (HTTP GET) http://localhost:5001/users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users_data)


# POST route for creating a new user 
@app.route('/users', methods=['POST'])
def create_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    dob = fake.date_of_birth()

    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'dob': dob,
    }
    return jsonify(user), 201

# PUT route for updating a user by ID 

# DELETE route for deleting a user by ID