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