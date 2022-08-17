from input_validation import InputVerification as validate
from display.message import Say

class MenuInput:
    """
    Class containing functions to request input from user
    to perform different menu tasks. 
    """

    def create_new_event():
        pass

    def show_all():
        pass

    def show_upcoming():
        pass

    def show_past():
        pass

    def search_events():
        pass

    def delete_event():
        # List all events, have user enter ID of desired event
        pass

    def select_diffent_calendar():
        pass

    def reset_calendar():
        pass

    def exit_session():
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
        new_event = {}

        Say.askfor_event_name()
        new_event['event_name'] = validate().verify(input())

        Say.askfor_event_type()
        new_event['event_type'] = validate().verify(input())

        Say.askfor_organizer()
        new_event['organizer'] = validate.verify(input())

        Say.askfor_location()
        new_event['location'] = validate.verify(input())

        Say.askfor_date()
        new_event['date'] = validate.verify_date(input())

        Say.askfor_time()
        new_event['time'] = validate.verify_time(input())

        return new_event

