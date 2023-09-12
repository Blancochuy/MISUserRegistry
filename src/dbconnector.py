from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.config.config import spreadsheet_id, SCOPES


class DBConnector:

    def __init__(self):

        # Sets up the credentials needed to do any communication with Google sheets
        self.credentials = service_account.Credentials. \
            from_service_account_file("config/credentials.json",
                                      scopes=SCOPES)

        # This is what we are using to tell google what we are attempting to communicate with
        self.service = build("sheets", "v4", credentials=self.credentials)

        # This should set up the connection to the Google sheet and allow for communication between python and Google
        request = self.service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=[], includeGridData=False)
        self.sheet_props = request.execute()

        # This is the current location that we can use so row 2 should be the first available column if there is 0 users
        self.location = int(self.service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range="A2:A2").execute().get('values', [])[0][0]) + 2

    def get_name(self):
        return self.sheet_props["properties"]["title"]

    def get_values(self, range_name=None):
        """
        Retrieves the values from a range that is input
        :param
            range_name: range of values to be retrieved EX: (A1:F1)
        :return
            values: list of lists, values from each row corresponded
        """
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id, range=range_name).execute()
            rows = result.get('values', [])
            return rows
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def update_values(self, range_name=None, value_input_option="USER_ENTERED", values=None):
        """
        updates a given range in the sheet
        :param
            range_name: range of values to be updated
            value_input_option: How the values are to be updated (USER_ENTERED)
            values: values that will be sent into the sheets
        """
        try:
            body = {
                'values': values
            }
            result = self.service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id, range=range_name,
                valueInputOption=value_input_option, body=body).execute()
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error
