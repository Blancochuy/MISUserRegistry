from google.oauth2 import service_account
from googleapiclient.discovery import build

from config.config import spreadsheet_id

class DBConnector():

    def __init__(self):
        self.credentials = service_account.Credentials.\
            from_service_account_file("config/credentials.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
        self.service = build("sheets", "v4", credentials=self.credentials)

        request = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False)
        self.sheet_props = request.execute()

    def get_name(self):
        print(self.sheet_props["properties"]["title"])
