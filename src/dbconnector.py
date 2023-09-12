import google
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.config.config import spreadsheet_id

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


class DBConnector:

    def __init__(self):

        self.credentials = service_account.Credentials. \
            from_service_account_file("config/credentials.json",
                                      scopes=SCOPES)
        self.service = build("sheets", "v4", credentials=self.credentials)

        request = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False)
        self.sheet_props = request.execute()

    def get_name(self):
        print(self.sheet_props["properties"]["title"])

    def get_values(self, range_name):
        """
        Creates the batch_update the user has access to.
        Load pre-authorized user credentials from the environment.
        """
        # pylint: disable=maybe-no-member
        try:
            service = build('sheets', 'v4', credentials=self.credentials)

            result = service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=range_name).execute()
            rows = result.get('values', [])
            print(rows)
            print(f"{len(rows)} rows retrieved")
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

