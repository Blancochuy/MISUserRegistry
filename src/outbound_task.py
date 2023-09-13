import errno

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
        :return: True on success
        """
        try:
            location = "B" + str(self.user_registry.location) + ":F" + str(self.user_registry.location)
            query = [fname, lname, email, phone, dates]
            if dates is None:
                query = [fname, lname, email, phone, date.today().strftime("%m/%d/%y")]

            self.user_registry.update_values(range_name=location, values=[query])

            # Add one more user to NumUsers
            self.user_registry.update_values(range_name="A2", values=[[self.user_registry.location+1]])
            return True
        except errno as e:
            return e

    def edit_user(self, fname, lname=None):
        """
        should allow for admin to change a users status
        :param
            fname: First Name
            lname: Last Name
        :return: True on success
        """





