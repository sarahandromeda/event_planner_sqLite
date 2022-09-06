from database.command import SQLCommand
from input.user_inputs import MenuInput

class SearchEvents:
    pass 
    """
    Creates a search instance containg the search option
    and search parameters as instance variables. Begin
    search by calling SearchEvents.setup_search(). Function
    will initialize search instance and complete search
    returning a list of results.  
    """
    def __init__(self, calendar, conn, cursor, choice, param, modifier):
        self.calendar = calendar
        self.conn = conn
        self.cursor = cursor
        self.choice = choice
        self.param = param
        self.modifier = modifier

    def setup_search(session):
        calendar = session.calendar
        connection = session.connection
        cursor = session.cursor
        search_option, param = MenuInput.get_search_params()
        param = tuple(param[0])
        modifier = param[1] if param[1] else None

        new_search = SearchEvents(
            calendar,
            connection, 
            cursor, 
            search_option, 
            param, 
            modifier
            )

        results = new_search.start_search()
        return results

    def start_search(self):
        """
        Generate command string based on search choice and modifier.
        Executes command using cursor and returns results. 
        """
        if self.choice == '1':
            cmd_string = SQLCommand.search_by_organizer(self.calendar)

        elif self.choice == '2':
            cmd_string = SQLCommand.search_by_location(self.calendar)

        elif self.choice == '3':
            if self.modifier == '+':
                cmd_string = SQLCommand.search_after_date(self.calendar)

            elif self.modifier == '-':
                cmd_string = SQLCommand.search_before_date(self.calendar)

            else:
                cmd_string = SQLCommand.search_by_date(self.calendar)

        elif self.choice == '4':
            if self.modifier == '+':
                cmd_string = SQLCommand.search_after_time(self.calendar)

            elif self.modifier == '-':
                cmd_string = SQLCommand.search_before_time(self.calendar)

            else:
                cmd_string = SQLCommand.search_by_time(self.calendar)

        self.cursor.execute(cmd_string, self.param)
        results = self.cursor.fetchall()
        return results


    

        