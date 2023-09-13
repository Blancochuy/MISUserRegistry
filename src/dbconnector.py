import gspread
from googleapiclient.errors import HttpError

from src.config.config import spreadsheet_id, SCOPES


class DBConnector:

    def __init__(self):
        gc = gspread.service_account(filename='config/credentials.json')
        self.db = gc.open_by_key(spreadsheet_id).sheet1

        self.location = int(self.db.get('A2').first())

    def get_name(self):
        # Gets the values of the first row, this is just a check
        return self.db.row_values(1)

    def get_values_row(self, row):
        """
        Retrieves the values from a range that is input
        :param
            row: what row we want to change
        :return
            values: all values in the row
        """
        try:
            rows = self.db.row_values(row)
            return rows
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def get_values_col(self, col):
        """
        Retrieves the values from a range that is input
        :param
            col: what row we want to change
        :return
            values: all values in the row
        """
        try:
            cols = self.db.col_values(col)
            return cols
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error

    def update_values(self, range_name=None, values=None):
        """
        updates a given range in the sheet
        :param
            range_name: range of values to be updated
            value_input_option: How the values are to be updated (USER_ENTERED)
            values: values that will be sent into the sheets
        """
        try:
            self.db.update(range_name, values)
        except HttpError as error:
            print(f"An error occurred: {error}")
            return error
