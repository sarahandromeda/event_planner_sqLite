from database.command import SQLCommand
from input.input_validation import InputVerification as validate
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

    def get_new_event(session):
        """
        Executes new_event function from NewEventInput class and
        recieves a tuple object representing user inputted values
        Returns tuple of new event values. 
        """
        new_event_values = NewEventInput.new_event(session)
        return new_event_values
        
    def get_search_params():
        """
        Displays search options and asks user to input choice.
        Depending on choice, request the search parameter from
        the user. Returns choice and tuple of parameter. 
        """
        Say.search_options()
        choice = validate.verify_search_menu(input())

        if choice == '1' or choice == '2':
            Say.askfor_parameter()
            param = validate.verify(input())
        elif choice == '3':
            Say.askfor_event_type()
            param = validate.verify_type(input())
        elif choice == '4':
            Say.askfor_search_date()
            param = validate.verify_search_date(input())
        elif choice == '5':
            Say.askfor_search_time()
            param = validate.verify_search_time(input())

        return choice, param

    def get_delete_event(session):
        """
        Lists all events, have user enter ID of event they would
        like to delete. Returns ID of selected event. 
        """
        Say.askfor_id()
        event_id = validate.verify(input())
        return event_id

    def get_diffent_calendar(session):
        """
        Displays all calendars and requests user to input ID 
        of the calendar they would like to change to.
        Returns ID of selected calendar.
        """
        sql_cmd = SQLCommand.show_all_calendars()
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
    """
    def new_event(session):
        """
        Requests input from users relevant to a new event for each 
        field represented in the database. Uses validation methods
        from input_validation module to verify correct inputs.
        Checks existence of related objects before adding to return. 
        Returns a tuple of entered values. Tuple must match the
        following order for SQL statement to work as intended:
        (<event_name>,<date>,<time>,<event_type>,<organizer>,<state>,<city>)
        """
        new_event = {}

        Say.askfor_event_name()
        new_event['event_name'] = validate.verify(input())

        Say.askfor_date()
        new_event['date'] = validate.verify_date(input())

        Say.askfor_time()
        new_event['time'] = validate.verify_time(input())

        Say.askfor_event_type()
        new_event['event_type'] = validate.verify_type(input())

        Say.askfor_organizer()
        new_event['organizer'] = validate.verify(input())

        Say.askfor_state()
        new_event['state_country'] = validate.verify(input())

        Say.askfor_city()
        new_event['city'] = validate.verify(input())

        values = [v for _,v in new_event.items()]
        return tuple(values)

    def _check_instance(session, new_event_input):
        """
        Checks if user input to a foreign key field has an
        existing match in related table.
        Accepts user input and checks to see if related table
        has an entry matching the user input. If not, create 
        an entry. 
        Returns ID of matching entry. 
        """
        for k,v in new_event_input.items():
            if k == 'organizer':
                session.cursor.execute(f"""
                    SELECT organizer_id
                    FROM organizers
                    WHERE name = {v};
                """)
                if len(session.cursor) > 0:
                    new_event_input['organizer'] = session.cursor[0]
                else:
                    session.cursor.execute(f"""
                        INSERT INTO organizers (name)
                        VALUES({v},);
                    """)
                    session.connection.commit()
                session.cursor.execute(f"""
                    SELECT organizer_id
                    FROM organizers
                    WHERE name = {v};
                """)
                new_event_input['organizer'] = session.cursor[0]
                
            elif k == 'state_country':
                pass
            elif k == 'city':
                pass
