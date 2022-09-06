# Main class welcomes user and requests them to select
# an existing calendar or create a new one
# Initialize session class with calendar name set
# to desired calendar
from os.path import exists, join
from config import settings
from database.connection import DBConnection
from database.menu import MenuAction
from database.set_up import SetUpDB
from display.message import Say

class Session:
    # Initialize session class setting selected calendar 
    # to selection from main
    """
    Creates a user session of the program. Sets calendar
    to currently selected calendar to use in databse
    commands. Creates connection and cursor objects.
    """
    def __init__(self):
        self.calendar = settings.DEFAULT_CALENDAR_NAME
        self.connection = DBConnection.create_connection(settings.DEFAULT_DB_FILE_NAME)
        self.cursor = self.connection.cursor()

    def change_calendar(self, new_calendar):
        self.calendar = new_calendar
    
    def begin(self):
        self._check_tables()
        Say.hello()
        while True:
            menu = MenuAction.menu_choice(self)
            if menu == 'exit':
                break
        Say.goodbye()

    def _check_tables(self):
        """
        Checks that database is created in expected folder
        otherwise calls to SetUpDB class. 
        """
        planner = join(settings.DB_FILE_LOCATION, settings.DEFAULT_DB_FILE_NAME)
        if not exists(planner):
            SetUpDB().generate()


if __name__ == '__main__':
    session = Session()
    session.begin()