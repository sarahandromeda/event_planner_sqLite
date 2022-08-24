from database.command import Command
from display.message import Say
from input.inputs import MenuInput
from database.search import SearchEvents

class MenuAction:
    """
    Contains display functions for the main menu, and 
    search menu. 
    """
    def menu_choice(session): 
        choice = MenuInput.menu_input()

        if choice == '1':
            values = MenuInput.get_new_event()
            MenuAction.create_new_event(session, values)

        elif choice == '2':
            MenuAction.show_all(session)

        elif choice == '3':
            MenuAction.show_upcoming(session)

        elif choice == '4':
            MenuAction.show_past(session)

        elif choice == '5':
            MenuAction.search_events(session)

        elif choice == '6':
            values = MenuInput.get_delete_event(session)
            MenuAction.delete_event(session, values)

        elif choice == '7':
            values = MenuInput.get_diffent_calendar(session)
            MenuAction.select_different_calendar(session, values)

        elif choice == '8':
            confirm = MenuInput.confirm_reset()
            if confirm == 'y':
                MenuAction.delete_all(session)
            else:
                Say.action_aborted()

        elif choice == '9':
            MenuAction.exit_session()

    def create_new_event(session, values):
        """
        Accepts a session object and values tuple.
        Generates SQL command and executes with supplied values.
        """
        sql_cmd = Command.create_event(session.calendar)
        session.cursor.execute(sql_cmd, values)
        session.connection.commit()
        Say.success()

    def show_all(session):
        """
        Accepts a session object housing connection and cursor.
        Generates SQL command string and executes command. Get
        selection from cursor object, display results as table.
        """
        sql_cmd = Command.show_all_events(session.calendar)
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.event_table(results)

    def show_upcoming(session):
        sql_cmd = Command.show_upcoming_events(session.calendar)
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.event_table(results)

    def show_past(session):
        sql_cmd = Command.show_past_events(session.calendar)
        session.cursor.execute(sql_cmd)
        results = session.cursor.fetchall()
        Say.event_table(results)

    def search_events(session):
        results = SearchEvents.setup_search(session)
        Say.event_table(results)

    def delete_event(session, event_id):
        sql_cmd = Command.delete_event(session.calendar)
        session.cursor.execute(sql_cmd, tuple(event_id))
        Say.confirm_deleted(event_id)

    def select_different_calendar(session, calendar_id):
        sql_calendar_select = Command.select_calendar()
        session.cursor.execute(sql_calendar_select, calendar_id)
        new_calendar = session.cursor.fetchone()
        session.change_calendar(new_calendar)
        Say.selected_calendar(new_calendar)

    def delete_all(session):
        sql_cmd = Command.delete_all_events(session.calendar)
        session.cursor.execute(sql_cmd)
        Say.success()

    def exit_session():
        pass
