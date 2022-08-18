from unittest import result
from database.command import Command
from display.menu import Menu
from input_validation import InputVerification as validate
from display.message import Say

class MenuInput:
    """
    Class containing functions to request input from user
    to perform different menu tasks. 
    """
    def menu_input(session):
        """
        Requests a menu input from user, executes method matching
        the menu option to get relevant input for action.
        """

        Say.show_menu()
        menu_choice = validate.verify_menu(input())

        if menu_choice == '1':
            MenuInput._create_new_event(session)
        elif menu_choice == '2':
            MenuInput._show_all(session)
        elif menu_choice == '3':
            MenuInput._show_upcoming(session)
        elif menu_choice == '4':
            MenuInput._show_past(session)
        elif menu_choice == '5':
            MenuInput._search_events(session)
        elif menu_choice == '6':
            MenuInput._delete_event(session)
        elif menu_choice == '7':
            MenuInput._select_diffent_calendar(session)
        elif menu_choice == '8':
            MenuInput._reset_calendar(session)
        elif menu_choice == '9':
            MenuInput._exit_session()

    def _create_new_event(session):
        """
        Executes new_event function from NewEventInput class and
        recieves a tuple object representing user inputted values
        Gets SQL command from Commands class and adds new event. 
        """
        new_event_values = NewEventInput.new_event()
        sql_cmd = Command.create_event(session.calendar)
        session.cursor.execute(sql_cmd, new_event_values)
        Say.success()

    def _show_all(session):
        """
        Generates SQL command string and executes command. Get
        selection from cursor object, display results as table.
        """
        sql_cmd = Command.show_all_events(session.calendar)
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.event_table(results)

    def _show_upcoming(session):
        sql_cmd = Command.show_upcoming_events(session.calendar)
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.event_table(results)

    def _show_past(session):
        sql_cmd = Command.show_past_events(session.calendar)
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.event_table(results)

    def _search_events(session):
        Say.search_options()
        results = validate.verify(input())
        if results == '1':
            SearchInput.get_organizer()
        elif results == '2':
            SearchInput.get_location()
        elif results == '3':
            SearchInput.get_type()
        elif results == '4':
            SearchInput.get_date()
        elif results == '5':
            SearchInput.get_time()

    def _delete_event(session):
        # List all events, have user enter ID of desired event
        MenuInput.show_all(session)
        Say.askfor_id()
        event_id = validate.verify(input())
        sql_cmd = Command.delete_event(session.calendar)
        session.cursor.execute(sql_cmd, tuple(event_id))
        Say.confirm_deleted(event_id)

    def _select_diffent_calendar(session):
        sql_cmd = Command.show_all_calendars()
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.calendar_table(results)
        Say.askfor_id()
        calendar_id = validate.verify(input())
        sql_calendar_select = Command.select_calendar()
        session.cursor.execute(sql_calendar_select, calendar_id)
        new_calendar = session.cursor.fetchone()
        session.select_diffent_calendar(new_calendar)
        Say.selected_calendar(new_calendar)

    def _reset_calendar(session):
        Say.confirm_reset()
        confirm = input().lower()
        if confirm == 'y':
            sql_cmd = Command.delete_all_events(session.calendar)
            session.cursor.execute(sql_cmd)
        else:
            Say.action_aborted()

    def _exit_session():
        pass

class SearchInput:
    """
    Class containing functions to request input from user
    about a search they would like to perform. 
    """
    
    def get_organizer():
        pass

    def get_location():
        pass

    def get_type():
        pass

    def get_date():
        # on date
        # before date
        # after date
        pass

    def get_time():
        # at time
        # before time
        # after time
        pass

class NewEventInput:
    """
    Class housing function to request input from user to create
    a new event.
    Returns new_event dict representing the fields as keys and
    inputs as the values.
    """
    def new_event():
        """
        Requests input from users relevant to a new event for each 
        field represented in the CSV file. Uses validation methods
        from input_validation module to verify correct inputs. 
        Returns a dictionary object with the keys representing the
        fields and the values representing the user's data. 
        """
        new_event = []

        Say.askfor_event_name()
        new_event.append(validate.verify(input()))

        Say.askfor_event_type()
        new_event.append(validate.verify(input()))

        Say.askfor_organizer()
        new_event.append(validate.verify(input()))

        Say.askfor_location()
        new_event.append(validate.verify(input()))

        Say.askfor_date()
        new_event.append(validate.verify_date(input()))

        Say.askfor_time()
        new_event.append(validate.verify_time(input()))

        return tuple(new_event)