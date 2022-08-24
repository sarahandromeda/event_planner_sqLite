# Main class welcomes user and requests them to select
# an existing calendar or create a new one
# Initialize session class with calendar name set
# to desired calendar
from config import settings
from database.connection import Connection

class Session:
    # Initialize session class setting selected calendar 
    # to selection from main
    """
    Creates a user session of the program. Sets calendar
    to currently selected calendar to use in databse
    commands. Creates connection and cursor objects.
    """
    def __init__(self):
        self.calendar = None
        self.connection = Connection.create_connection(settings.DEFAULT_DB_FILE_NAME)
        self.cursor = self.connection.cursor()

    def change_calendar(self, new_calendar):
        self.calendar = new_calendar
    
    def begin(self):
        pass

if __name__ == '__main__':
    # initialize session and run begin().
    pass