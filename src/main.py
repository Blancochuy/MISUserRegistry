from dbconnector import DBConnector

if __name__ == "__main__":
    # execute only if run as a script
    MISDB = DBConnector()
    MISDB.get_name()
    MISDB.secret_hash(MISDB.access_secret_version("config"))
