from dbconnector import DBConnector

if __name__ == "__main__":
    # execute only if run as a script
    MISDB = DBConnector()
    MISDB.get_name()
