# Make this class a mixin for class MainSession
class Command:
    """
    Collection of strings of SQL database execution
    statements. Functions take arguments to be interpolated
    into strings, returns new formed string.
    """

    def create_calendar(calendar_name):
        create_table = f"""
            CREATE TABLE IF NOT EXISTS {calendar_name} (
                event_name text NOT NULL,
                event_type text NOT NULL,
                organizer text NOT NULL,
                location text NOT NULL,
                date text NOT NULL,
                time text NOT NULL
                );
        """
        return create_table

    def create_event(calendar_name):    
        create_entry = f"""
            INSERT INTO {calendar_name} (event_name, event_type, organizer, location, date, time)
            VALUES(?,?,?,?,date(?),time(?))
        """
        return create_entry

    def update_event(calendar_name):
        update_entry = f"""
            UPDATE {calendar_name}
            SET event_name = ?,
                event_type = ?,
                organizer = ?,
                location = ?,
                date = ?,
                time = ?
            WHERE rowid = ?;
        """
        return update_entry

    def delete_event(calendar_name):
        delete_entry = f"""
            DELETE FROM {calendar_name} WHERE rowid = ?;
        """
        return delete_entry

    def delete_all_events(calendar_name):
        delete_all = f"""
            DELETE FROM {calendar_name};
        """
        return delete_all

    def show_all_calendars():
        query_all_calendars = """
            SELECT
                rowid,
                name
            FROM sqlite_master
        """
        return query_all_calendars

    def show_all_events(calendar_name):
        query_by_all = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name}
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_by_all

    def search_by_organizer(calendar_name):
        query_by_organizer = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                organizer = ?
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_by_organizer

    def search_by_location(calendar_name):
        query_by_location = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                location = ?
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_by_location

    def search_by_date(calendar_name):
        query_by_date = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                date = date(?)
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_by_date

    def search_before_date(calendar_name):
        query_before_date = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                date < date(?)
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_before_date

    def search_after_date(calendar_name):
        query_after_date = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                date > date(?)
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_after_date

    def search_by_time(calendar_name):
        query_by_time = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                time = time(?)
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_by_time

    def search_before_time(calendar_name):
        query_before_time = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                time < time(?)
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_before_time

    def search_after_time(calendar_name):
        query_after_time = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                time > time(?)
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_after_time

    def show_past_events(calendar_name):
        query_by_past = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                date < date('now') AND
                time < time('now')
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_by_past

    def show_upcoming_events(calendar_name):
        query_by_upcoming = f"""
            SELECT
                rowid,
                event_name,
                event_type,
                organizer,
                location,
                date,
                time 
            FROM {calendar_name} 
            WHERE 
                date > date('now') and
                time > time('now')
            ORDER BY
                date DESC,
                time DESC;
        """
        return query_by_upcoming