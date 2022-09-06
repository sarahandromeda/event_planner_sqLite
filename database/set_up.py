import config.settings as settings
from database.command import SQLCommand
from database.connection import DBConnection

class SetUpDB:
    """
    Class to be called on first run of program or if no tables
    exist in default database defined in settings. 
    """

    CLASS_FUNCS = [
        '_event_types_table', 
        '_organizers_table', 
        '_states_table', 
        '_cities_table',
        '_default_calendar_table'
        ]

    EVENT_TYPES = [
        'Concert',
        'Conference',
        'Convention',
        'Exhibition'
        'Festival',
        'Graduation',
        'Party',
        'Seminar',
        'Sports/Competition',
        'Trade Show/Product Launch',
        'Wedding'
    ]

    def generate(self):
        """
        Will generate database and call necessary functions
        to initialize all tables. 
        """
        self.conn = DBConnection.create_connection(settings.DEFAULT_DB_FILE_NAME)
        self.cur = self.conn.cursor()
        for func in self.CLASS_FUNCS:
            getattr(self, func)(self)
        self.conn.commit()
        self.conn.close()

    def _event_types_table(self):
        """
        Event type table will be preset with all acceptable event types.
        No entries will be dynamically created, user can only select
        from the entries preset in the table.
        """
        self.cur.execute("""
            CREATE TABLE event_types (
                event_type_id integer PRIMARY KEY,
                event_type text NOT NULL UNIQUE
            );
        """)
        for type in self.EVENT_TYPES:
            self.cur.execute(f"""
                INSERT INTO event_types (event_type)
                VALUES({type},);
            """)
            self.conn.commit()

    def _organizers_table(self):
        self.cur.execute("""
            CREATE TABLE organizers (
                organizer_id integer PRIMARY KEY,
                organizer text NOT NULL UNIQUE
            );
        """)

    def _states_table(self):
        self.cur.execute("""
            CREATE TABLE states_countries (
                state_id integer PRIMARY KEY,
                state_country text NOT NULL 
            );
        """)

    def _cities_table(self):
        self.cur.execute("""
            CREATE TABLE cities (
                city_id integer PRIMARY KEY,
                city text NOT NULL,
                state_id integer,
                FOREIGN KEY (state_id)
                    REFERENCES states_countries (state_id)
                    ON DELETE SET NULL
            );
        """)

    def _default_calendar_table(self):
        self.cur.execute(SQLCommand.create_calendar(
            settings.DEFAULT_CALENDAR_NAME
        ))
