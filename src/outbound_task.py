from dbconnector import DBConnector
from datetime import date


# Class that will have all the functions that a user would need to use to communicate with Google sheets
class Userinput:

    def __init__(self):
        self.user_registry = DBConnector()

    def add_user(self, fname, lname, email, phone, dates=None):
        """
        Adds a user to the registry
        :param
             fname: First name
             lname: Last name
             email: Email of member
             phone: Phone number of user
             date: mm/dd/yy
        :return: bool
        """

        location = "B" + str(self.user_registry.location) + ":F" + str(self.user_registry.location)
        print(location)
        query = [fname, lname, email, phone, dates]
        if dates is None:
            query = [fname, lname, email, phone, date.today().strftime("%m/%d/%y")]

        self.user_registry.update_values(range_name=location, values=[query])

        # Add one more user to NumUsers
        self.user_registry.update_values(range_name="A2:A2", values=[[self.user_registry.location-1]])

        return True
