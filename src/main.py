from dbconnector import DBConnector
from outbound_task import Userinput

if __name__ == "__main__":
    # execute only if run as a script
    DB = Userinput()
    DB.add_user('Sebastian', 'Hermann', 'sebati@gmail.com', '6513525903')
