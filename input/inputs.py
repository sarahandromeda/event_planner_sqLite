from database.command import Command
from database.menu import MenuAction
from input_validation import InputVerification as validate
from display.message import Say

class MenuInput:
    """
    Class containing functions to request input from user
    to perform different menu tasks. 
    """
    def menu_input():
        """
        Displays menu options, and requests input from user. 
        Verifies that response is a valid menu option a
        returns the choice. 
        """
        Say.show_menu()
        menu_choice = validate.verify_menu(input())
        return menu_choice

    def get_new_event():
        """
        Executes new_event function from NewEventInput class and
        recieves a tuple object representing user inputted values
        Returns tuple of new event values. 
        """
        new_event_values = NewEventInput.new_event()
        return new_event_values
        
    def get_search_params():
        """
        Displays search options and asks user to input choice.
        Depending on choice, request the search parameter from
        the user. Returns choice and tuple of parameter. 
        """
        Say.search_options()
        choice = validate.verify(input())

        if choice == '1' or choice == '2':
            Say.askfor_parameter()
            param = validate.verify(input())
        elif choice == '3':
            Say.askfor_search_date()
            param = validate.verify_search_date(input())
        elif choice == '4':
            Say.askfor_search_time()
            param = validate.verify_search_time(input())

        return choice, param

    def get_delete_event(session):
        """
        Lists all events, have user enter ID of event they would
        like to delete. Returns ID of selected event. 
        """
        MenuAction.show_all(session)
        Say.askfor_id()
        event_id = validate.verify(input())
        return event_id

    def get_diffent_calendar(session):
        """
        Displays all calendars and requests user to input ID 
        of the calendar they would like to change to.
        Returns ID of selected calendar.
        """
        sql_cmd = Command.show_all_calendars()
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.calendar_table(results)
        Say.askfor_id()
        calendar_id = validate.verify(input())
        return calendar_id
        
    def confirm_reset():
        """
        Displays confirmation message and asks user to confirm.
        Returns user's response. 
        """
        Say.confirm_reset()
        confirm = input().lower()
        return confirm

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