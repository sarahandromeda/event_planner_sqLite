import time
from media import art

class Say:
    """
    Class methods that print relevant messages to the console.
    """

# General Display Messages
    def hello():
        print(art.header)
        time.sleep(1)
        print("""
------------------------------
Welcome to your Event Manager

To create a new event, simply enter the number '1' to begin.
You will be prompted for details about the event to create.
After you have at least 1 event, you can use the other menu
options to show upcoming or past events, delete events search 
events by location, time, and more!
-------------------------------
        """, end='')
        time.sleep(1)

    def goodbye():
        print("See you next time!")
        print('Closing planner', end='')
        for i in range(5):
            print('.', end='', flush=True)
            time.sleep(0.3)
        print('')

    def proceed():
        print('\nPress enter to continue.\n')

    def choose_calendar(calendars):
        print(
            "Please select the calendar you would like to work on."
            )
        for i in range(len(calendars)):
            print(f"""
        {i}) {calendars[i]}
            """)

    def show_menu():
        print("""
Please select from the following options. 
Enter a single number corresponsing to the choice.

    1) Create an Event          6) Delete Event

    2) Show All Events          7) Select Different Calendar

    3) Show Upcoming Events     8) Reset Calendar**   

    4) Show Past Events         9) Exit

    5) Search Events

** This menu option is irreversible and will delete all of
your data. Use with caution.
        """)

    def search_options():
        print("""
Please enter numbers corresponding to the fields you
would like to search.

    1) Search by Organizer      4) Search by Date

    2) Search by Location       5) Search by Time
    
    3) Search by Type
        """)
    
    def event_string(data_dict):
        # NEED TO FIX THIS MESSAGE
        # CHANGE THIS TO LIST ROWS IN TABLE FORM
        """
        Takes a list of event dict objects, loops through them, and
        prints a human readable string of each event.
        """
        for event in data_dict:
            event_name = event['event_name']
            event_type = event['event_type']
            organizer = event['organizer']
            start_date = event['start_date']
            formatted_time = start_date.strftime("%A, %B %-d, %Y at %-I:%M %p")
            location = event['location']
            print(f"""
{organizer} is hosting {event_name}, a {event_type}, 
on {formatted_time} in {location}!
            """)

# Input Prompt Messages

    def askfor_event_name():
        print('\nPlease enter name of event.\n')

    def askfor_event_type():
        print(
            "\nPlease enter the type of the event.\n" +
            "Ex. Party, Reunion, Convention, Festival, etc.\n")

    def askfor_organizer():
        print(
            '\nPlease enter the name of the event organizer.\n' + 
            'Include, at minimum, a first name.\n'
            )

    def askfor_location():
        print(
            '\nPlease enter the location of the event.\n' +
            'Include, at minimum, the state.\n'
            )

    def askfor_date():
        print(
            '\nPlease enter the date of the event.\n' +
            'Use YYYY/MM/DD format.\n'
            )

    def askfor_time():
        # Need to fix input on this to convert 04:30PM
        # to 16:00:00 format
        print(
            '\nPlease enter the time of the event.\n' +
            'Use HH:MM format also indicating AM or PM.\n' +
            'Ex. 04:30 PM\n'
            )

# Confirmation and Error messages

    def confirm_deletion(selection_dict):
        print("""
            
            Please review the selection(s):

            """)
        count = 0
        for event in selection_dict:
            print(
                f"{count}) {event['organizer']}'s " +
                f"{event['event_type']} " +
                f"on {event['start_datetime'].date()} " +
                f"at {event['start_datetime'].time()}\n\n"
            )
            count += 1
        print("""

            Enter the numbers of the events you would like to delete.
            Ex. "0 5 10" to delete events numbered respectively.
            To abort, type 'n' or just press enter.

            """)

    def confirm_deleted(object):
        print(f'\n{object} sucessfully deleted.\n')

    def invalid_input(response):
        print(f'\n{response} is invalid.\n')

    def invalid_date(response):
        print(
            f'\n{response} is invalid.\n' +
            'Please enter a date in format YYYY/MM/DD.\n'
            )

    def invalid_time(response):
        print(
            f'\n{response} is invalid.\n' +
            'Please enter time in HH:MM AM (or PM) format.\n'
            )