from ..database.command import CommandMixin

class Session(CommandMixin):
    # Initialize session class setting selected calendar 
    # to selection from main
    """
    Creates a user session of the program. Sets calendar
    to currently selected calendar to use in databse
    commands.
    """
    def __init__(self, calendar):
        self.calendar = calendar

    def change_calendar(self, new_calendar):
        self.calendar = new_calendar