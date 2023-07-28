import requests
from faker import Faker
from models import user  # Import the user model
from flask import Flask, request, jsonify

# Set up Faker
fake = Faker()

# Endpoint URL for the Flask app
base_url = "http://localhost:5001"

# Create a Flask app instance
app = Flask(__name__)

# Function to create a new user
def create_user():
    # Generate user data using Faker
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    dob = fake.date_of_birth()

    # Convert the dob date object to a string representation
    dob_str = dob.strftime("%Y-%m-%d")

    # Create the user object
    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'dob': dob_str,
    }

    # Make the POST request to create the user
    response = requests.post(f"{base_url}/users", json=user_data)

    if response.status_code == 201:
        # If the user was successfully created, return the user data
        return response.json()
    else:
        # If there was an error creating the user, return None
        print(response.text) # print error message 
        return None

if __name__ == "__main__":
    # Create 100 users using the `create_user()` function
    for _ in range(100):
        user = create_user()
        if user:
            print(f"Created user: {user}")
        else:
            print("Failed to create user")
