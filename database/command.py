class SQLCommand:
    """
    Collection of strings of SQL database execution
    statements. Functions take arguments to be interpolated
    into strings, returns new formed string.
    """

    def create_calendar(calendar_name):
        create_table = f"""
            CREATE TABLE IF NOT EXISTS {calendar_name} (
                event_id integer PRIMARY KEY,
                event_name text NOT NULL,
                event_type_id integer,
                organizer_id integer,
                state_id integer,
                city_id integer,
                date text NOT NULL,
                time text NOT NULL,
                FOREIGN KEY (event_type_id)
                    REFERENCES event_types (event_type_id)
                    ON DELETE SET NULL,
                FOREIGN KEY (organizer_id)
                    REFERENCES organizers (organizer_id)
                    ON DELETE SET NULL,
                FOREIGN KEY (state_id)
                    REFERENCES states_countries (state_id)
                    ON DELETE SET NULL,
                FOREIGN KEY (city_id)
                    REFERENCES cities (city_id)
                    ON DELETE SET NULL,
            );
        """
        return create_table

    def create_event(calendar_name):    
        create_entry = f"""
            INSERT INTO calendar (
                event_name, 
                event_type_id, 
                organizer_id, 
                state_id, 
                city_id, 
                date, 
                time
                )
            SELECT
                ?,
                t.type_id,
                o.organizer_id,
                s.state_id,
                c.city_id,
                date(?),
                time(?)
            FROM 
                event_types AS t,
                organizers AS o,
                states_countries AS s,
                cities AS c
            WHERE
                t.event_type = ? AND
                o.organizer = ? AND
                s.state_country = ? AND
                c.city = ?
            ;
        """
        # Where the first '?' shall represent the event_name
        return create_entry

    def update_event(calendar_name):
        update_entry = f"""
            UPDATE {calendar_name}
            SET event_name = ?,
                event_type_id = ?,
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

    def select_calendar():
        select_calendar = """
            SELECT
                name
            FROM sqlite_master
            WHERE
                rowid = ?
        """
        return select_calendar

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
                organizer LIKE '%' || ? || '%'
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
                location LIKE '%' || ? || '%'
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
                date = date(?) OR
                strftime('%m', date) = strftime('%m', date(?)) OR
                strftime('%Y', date) = strftime('%Y', date(?))
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

    def select_event_types():
        """
        Selects all event types in related table
        to display as menu option.
        """
        select_types = """
            SELECT
                event_type_id,
                event_type
            FROM 
                event_types;
        """
        return select_types