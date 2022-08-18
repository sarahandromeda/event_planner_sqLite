import time
from media import art

class Say:
    """
    Class methods that print relevant messages to the console.
    """

############################
# General Display Messages #
############################

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
Please enter a number corresponding to a field to search by.

    1) Search by Organizer*      4) Search by Date

    2) Search by Location*       5) Search by Time
    
    3) Search by Type*
        
*When searching by these fields, you can enter the full 
value or just a single letter to return events that have 
that single letter within the value being searched. 
EX. Searching 'c' for location would return locations in
Colorado, South Carolina, San Fransico as they all contain
the letter 'c'.
        """)
    
    def calendar_table(calendar_list):
        """
        Takes the list of calendars and displays as a table.
        """
        print("""
----------------------
| ID | Calendar Name |
----------------------  
        """)
        for calendar in calendar_list:
            calendar_id = calendar[0]
            calendar_name = calendar[1]
            print(
                f"| {calendar_id} |" +
                f"| {calendar_name} |"
            )
        print("""
----------------------
        """)

    def event_table(data_list):
        """
        Takes a list of event dict objects, loops through them, and
        displays results as a table.
        """
        # Print table header
        print("""
---------------------------------------------------------------------
| ID | Event Name | Event Type | Organizer | Location | Date | Time |
---------------------------------------------------------------------
        """)
        for event in data_list:
            event_id = event[0]
            event_name = event[1]
            event_type = event[2]
            organizer = event[3]
            location = event[4]
            date = event[5]
            time = event[6]
            print(
                f"|{event_id}|" +
                f"|{event_name}|" +
                f"{event_type}|" +
                f"{organizer}" +
                f"{location}|" +
                f"{date}|" +
                f"{time}|"
            )
        print("""
---------------------------------------------------------------------
        """)
#########################
# Input Prompt Messages #
#########################

# New Event Messages

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

# Search Input Messages
    def askfor_parameter():
        print(
            '\nPlease enter a search parameter.\n' + 
            'Can be full value or partial. Case insensitive.\n'
            )

    def askfor_id():
        print(
            "\nPlease enter the ID number of the item you would like to select.\n"
        )

###################################
# Confirmation and Error messages #
###################################

    def success():
        print("\nAction Successful!\n")

    def action_aborted():
        print('\nAborting...\n')

    def general_error():
        print('\nSorry, but an error has occurred. Please try again.\n')

    def selected_calendar(calendar):
        print(f"\nYou are now working on your {calendar} calendar.\n")

    def confirm_reset():
        print('\nAre you sure you want to clear this calender? y/n\n')

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