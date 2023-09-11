from google.cloud import secretmanager
from google.oauth2 import service_account
from googleapiclient.discovery import build

from config.config import spreadsheet_id

import hashlib

class DBConnector():

    def __init__(self):
        self.credentials = service_account.Credentials.\
            from_service_account_file("src/config/credentials.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
        self.service = build("sheets", "v4", credentials=self.credentials)

        request = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False)
        self.sheet_props = request.execute()

    def access_secret_version(self, secret_id, version_id="latest"):
        # Create the Secret Manager client.
        client = secretmanager.SecretManagerServiceClient()

        # Build the resource name of the secret version.
        name = f"projects/MISUserRegistry/secrets/{secret_id}/versions/{version_id}"

        # Access the secret version.
        response = client.access_secret_version(name=name)

        # Return the decoded payload.
        return response.payload.data.decode('UTF-8')

    def secret_hash(self, secret_value):
        # return the sha224 hash of the secret value
        return hashlib.sha224(bytes(secret_value, "utf-8")).hexdigest()

    def get_name(self):
        print(self.sheet_props["properties"]["title"])
