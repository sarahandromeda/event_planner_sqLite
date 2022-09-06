import os
import sqlite3
from sqlite3 import Error
import config.settings as settings

class DBConnection:
    def create_connection(file_name):
        """
        Tries to open a connection the the desired database.
        Returns connection object if successful.
        On first run, or if no defaultDB exists in expected
        folder, defaultDB will be created.
        """
        connection = None
        try:
            if file_name == ':memory:':
                connection = sqlite3.connect(file_name)
            else:
                connection = sqlite3.connect(
                    os.path.join(settings.DB_FILE_LOCATION, file_name)
                )
            return connection
        except Error as e:
            print(f"There was an error opening the database, {e}")

        
