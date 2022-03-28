import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from src.settings.constants import CREDENTIALS_FILE
from src.settings.constants import SCOPES
from src.settings.constants import TOKEN_FILE


def get_credentials() -> Credentials:
    credentials = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.isfile(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        credentials = refresh_token(credentials)

    # Save the credentials for the next run
    save_token(credentials)

    return credentials


def refresh_token(credentials: Credentials) -> Credentials:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        if not os.path.isfile(CREDENTIALS_FILE):
            with open(CREDENTIALS_FILE, "w") as file:
                file.write("")

        flow = InstalledAppFlow.from_client_secrets_file(
            CREDENTIALS_FILE, SCOPES
        )
        credentials = flow.run_local_server(port=0)

    return credentials


def save_token(credentials: Credentials) -> None:
    with open(TOKEN_FILE, "w") as token:
        token.write(credentials.to_json())
