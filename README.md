# WHO Care 

This is World Health Organization Care backend app using Python, Flask, Django, and Postman on the server side. 

### Home Route
When open http://localhost:5001/ in browswer or fetch get route in Postman, you should be able to see this message, "Welcome to World Health Organization Care App!".

# Installation 

Check version for Python3 `python3 --version`

### Setup Virtual Environment 
`python3 -m venv venv`

### Activate the virtual environment:
`source venv/bin/activate`

### Install pymongo:
`pip install pymongo`

### Install django:
- Django: `pip install django` 
- check version `python -m django --version`

### Install flask:
- Flask: `pip install flask` 
- check version `python -m flask --version`

### Install Test:
Database Testing Tools: `pip install pytest`

### ICD API Authentication
- Register on the ICD API site (https://icd.who.int/icdapi).
- Click on the Register link and follow the instructions
- Once register and login, you may click on the `view API access key` to get your `clientid` and `clientsecret`. 

### ICD APIs OAUTH2 Authentication 
- Install Required Python libraries for making HTTP requests and handling OAuth 2.0 authentication access to API endpoint (similar to what the C# code) `pip install requests oauthlib`

- Token endpoint: https://icdaccessmanagement.who.int/connect/token 
- Disclaimer: tokens are valid for about 1 hour and after that one has to get a new one

**Convert C# code sample using .NET to Python**

**oauth.py**
```
import os
from dotenv import load_dotenv
import requests 
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def get_access_token():
    # Load environment variables from .env file
    load_dotenv()

    token_endpoint = "https://icdaccessmanagement.who.int/connect/token"
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    scope = "icdapi_access"

    oauth2_client = BackendApplicationClient(client_id=client_id)
    oauth2_session = OAuth2Session(client=oauth2_client)
    token = oauth2_session.fetch_token(
        token_url=token_endpoint,
        client_id=client_id,
        client_secret=client_secret,
        scope=scope
    )
    return token['access_token']  
```

**app.py**
```
import os
from oauth import get_access_token
import requests

# Access the secret session variables 
SECRET_SESSION = os.getenv("your secret session")
SECRET_SESSION = os.getenv("your secret session")

# Define Routes and Handlers
@app.route('/testPoint') # localhost:5001/testPoint show jsonify icd entity 
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
```

### Start Server in zsh Terminal 
`python app.py`

# References 
- ICD API (https://icd.who.int/icdapi)