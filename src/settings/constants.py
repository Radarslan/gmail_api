import os

from decouple import config

# If modifying these scopes, delete the file src/settings/token.json
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

# CLIENT_ID = config("CLIENT_ID")
# CLIENT_SECRET = config("CLIENT_SECRET")

TOKEN_FILE = os.path.join("src", "settings", "token.json")
CREDENTIALS_FILE = os.path.join("src", "settings", "credentials.json")

RECEIVER = config("RECEIVER")
SENDER = config("SENDER")
