import unittest
from unittest import TestCase
import time
from database.connection import DBConnection
from database.command import SQLCommand

"""
Tests components in command.py file.
"""

class CreationSQLCommandTest(TestCase):
    def setUp(self):
            """
            Sets up tests by creating connection and cursor.
            """
            self.conn = DBConnection.create_connection(':memory:')
            self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_create_calendar(self):
        """
        Test that command makes a valid table named 'new'
        inside the database. Asserts that in list of
        master tables, there is one named 'new'.
        """
        cmd_string = SQLCommand.create_calendar('new')
        self.cursor.execute(cmd_string)
        self.conn.commit()
        self.cursor.execute("""
            SELECT * 
            FROM sqlite_master
        """)
        for result in self.cursor.fetchall():
            if 'new' in result:
                self.assertIn('new', result)

    def test_create_event(self):
        """
        Test that command makes a new event with valid
        values. Try to select row based on given inputs
        and assert that an object was selected.
        """
        # Must first create table in memory db
        cmd_string = SQLCommand.create_calendar('new')
        self.cursor.execute(cmd_string)
        self.conn.commit()

        cmd_string = SQLCommand.create_event('new')
        values = (
            'Birthday Bash', 
            'Party', 
            'Sarah', 
            'Colorado',
            '2023-03-15',
            '16:30:00'
            )
        self.cursor.execute(cmd_string, values)
        self.conn.commit()
        self.cursor.execute("""
            SELECT *
            FROM new
            WHERE
                event_name = 'Birthday Bash' and
                event_type = 'Party' and
                organizer = 'Sarah' and
                location = 'Colorado' and
                date = date('2023-03-15') and
                time = time('16:30:00')
        """)
        self.assertTrue(self.cursor.fetchall())

class DatabaseSQLCommandTest(TestCase):
    def setUp(self):
        """
        Sets up tests by creating connection, cursor, table,
        and adding 2 events to the table with different values.
        """
        self.conn = DBConnection.create_connection(':memory:')
        self.cursor = self.conn.cursor()

        cmd_string = SQLCommand.create_calendar('new')
        self.cursor.execute(cmd_string)
        self.conn.commit()

        cmd_string = SQLCommand.create_event('new')
        values = (
            'Birthday Bash', 
            'Party', 
            'Sarah', 
            'Colorado',
            '2023-03-15',
            '16:30:00'
            )
        self.cursor.execute(cmd_string, values)
        self.conn.commit()

        cmd_string = SQLCommand.create_event('new')
        values = (
            '10 Years Gone', 
            'Reunion', 
            'Chris', 
            'Pennsylvania',
            '2023-05-15',
            '11:00:00'
            )
        self.cursor.execute(cmd_string, values)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_update_event(self):
        """
        Test that command method can update values of entry.
        Update event_name and assert that value is equal to
        input.
        """
        self.cursor.execute("""
            SELECT 
                event_name,
                event_type,
                organizer,
                location,
                date,
                time,
                rowid
            FROM new
        """)
        # Fetch first entry from selection
        entry = list(self.cursor.fetchone())
        cmd_string = SQLCommand.update_event('new')

        # The second value of entry is event_name
        entry[0] = 'Super Awesome Birthday Party'
        # Must pass values as tuple
        self.cursor.execute(cmd_string, tuple(entry))
        self.conn.commit()
        self.cursor.execute("""
            SELECT event_name
            FROM new
            WHERE rowid = 1
        """)
        selection = self.cursor.fetchone()
        self.assertEqual(selection[0], 'Super Awesome Birthday Party')

    def test_delete_event(self):
        """
        Test that command correctly selects and deletes 
        entry. Creates a test entry, fetches the rowid of
        new entry, passes rowid as value for delete command.
        Try to select row with given id after deletion, and
        assert that no selection is made. 
        """
        cmd_string = SQLCommand.create_event('new')
        values = (
            'test', 
            'test', 
            'test', 
            'test',
            '2023-03-15',
            '16:30:00'
            )
        self.cursor.execute(cmd_string, values)
        self.conn.commit()

        self.cursor.execute("""
            SELECT 
                rowid,
                event_name
            FROM new
        """)
        new_item = self.cursor.fetchall()[-1]
        new_item_id = new_item[0]

        cmd_string = SQLCommand.delete_event('new')
        self.cursor.execute(cmd_string, (new_item_id,))
        self.conn.commit()

        self.cursor.execute(f"""
            SELECT *
            FROM new
            WHERE rowid = {new_item_id}
        """)
        selection = self.cursor.fetchall()
        self.assertFalse(selection)
    
    def test_delete_all_events(self):
        """
        Tests that all events are deleted when run.
        Creates 2 test entries before deletion.
        Tries to select any entry in 'new' table,
        asserts that nothing is selected.
        """
        cmd_string = SQLCommand.delete_all_events('new')
        self.cursor.execute(cmd_string)
        self.conn.commit()
        
        self.cursor.execute("""
            SELECT * FROM new
        """)
        selection = self.cursor.fetchall()
        self.assertFalse(selection)

class QuerySQLCommandTest(TestCase):
    def setUp(self):
        """
        Sets up tests by creating connection, cursor, table,
        and adding 2 events to the table with different values.
        """
        self.conn = DBConnection.create_connection(':memory:')
        self.cursor = self.conn.cursor()

        cmd_string = SQLCommand.create_calendar('new')
        self.cursor.execute(cmd_string)
        self.conn.commit()

        cmd_string = SQLCommand.create_calendar('test')
        self.cursor.execute(cmd_string)
        self.conn.commit()

        cmd_string = SQLCommand.create_event('new')
        values = (
            'Birthday Bash', 
            'Party', 
            'Sarah', 
            'Colorado',
            '2023-03-15',
            '16:30:00'
            )
        self.cursor.execute(cmd_string, values)
        self.conn.commit()

        cmd_string = SQLCommand.create_event('new')
        values = (
            '10 Years Gone', 
            'Reunion', 
            'Chris', 
            'Pennsylvania',
            '2022-05-15',
            '11:00:00'
            )
        self.cursor.execute(cmd_string, values)
        self.conn.commit()

    def tearDown(self):
        self.conn.close()

    def test_show_all_calendars(self):
        """
        Test that command returns all created tables,
        representing calendars, in the database. 
        """
        cmd_string = SQLCommand.show_all_calendars()
        self.cursor.execute(cmd_string)
        selection = self.cursor.fetchall()
        self.assertEqual(len(selection), 2)

    def test_show_all_events(self):
        """
        Test that command returns all rows in database.
        Set up should create 2 objects. Call command
        and assert that all 2 objects get selected. 
        """
        cmd_string = SQLCommand.show_all_events('new')
        self.cursor.execute(cmd_string)
        selection = self.cursor.fetchall()
        self.assertEqual(len(selection), 2)

    def test_search_by_organizer(self):
        """
        Test that command returns only events with 'Sarah'
        as the organizer. Test that command returns only
        events whose organizer has an 's' in their name.
        Loops through selection and asserts 
        that index 2 (the organizer) is equal to 'Sarah'
        """
        cmd_string = SQLCommand.search_by_organizer('new')
        values = ('Sarah',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Organizer will be the item in index 3 of selected rows
        for row in selection:
            self.assertIn('Sarah', row[3])

        # Test that command returns all events whose organizer has
        # the value anywhere in the name
        values = ('s',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        print(selection)
        # Organizer will be the item in index 3 of selected rows
        for row in selection:
            self.assertIn('s', row[3].lower())
        
    
    def test_search_by_location(self):
        """
        Tests that command returns only events with 
        'Pennsylvania' as the location.
        """
        cmd_string = SQLCommand.search_by_location('new')
        values = ('Pennsylvania',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Location will be the item in index 4 of selected rows
        for row in selection:
            self.assertEqual(row[4], 'Pennsylvania')
        

    def test_search_by_date(self):
        cmd_string = SQLCommand.search_by_date('new')
        values = ('2023-03-15','2023-03-15','2023-03-15')
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Date will be the item in index 5 of selected rows
        for row in selection:
            self.assertEqual(row[5], '2023-03-15')

    def test_search_before_date(self):
        cmd_string = SQLCommand.search_before_date('new')
        values = ('2023-02-15',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Date will be the item in index 5 of selected rows
        for row in selection:
            self.assertTrue(row[5] < '2023-02-15')

    def test_search_after_date(self):
        cmd_string = SQLCommand.search_after_date('new')
        values = ('2022-01-01',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Date will be the item in index 5 of selected rows
        for row in selection:
            self.assertTrue(row[5] > '2022-01-01')

    def test_search_by_time(self):
        cmd_string = SQLCommand.search_by_time('new')
        values = ('11:00:00',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Time will be the item in index 6 of selected rows
        for row in selection:
            self.assertEqual(row[6], '11:00:00')

    def test_search_before_time(self):
        cmd_string = SQLCommand.search_before_time('new')
        values = ('12:00:00',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Time will be the item in index 6 of selected rows
        for row in selection:
            self.assertTrue(row[6] < '12:00:00')

    def test_search_after_time(self):
        cmd_string = SQLCommand.search_after_time('new')
        values = ('16:00:00',)
        self.cursor.execute(cmd_string, values)
        selection = self.cursor.fetchall()
        # Time will be the item in index 6 of selected rows
        for row in selection:
            self.assertTrue(row[6] > '16:00:00')

    def test_show_past_events(self):
        cmd_string = SQLCommand.show_past_events('new')
        self.cursor.execute(cmd_string)
        selection = self.cursor.fetchall()
        datetime_now = time.strftime('%Y-%m-%d %H:%M:%S')
        for event in selection:
            # Assert that date(index 5) and time(index 6) are less than now
            event_datetime = event[5] + " " + event[6]
            self.assertTrue(event_datetime < datetime_now)

    def test_show_upcoming_events(self):
        cmd_string = SQLCommand.show_upcoming_events('new')
        self.cursor.execute(cmd_string)
        selection = self.cursor.fetchall()
        datetime_now = time.strftime('%Y-%m-%d %H:%M:%S')
        for event in selection:
            # Assert that date(index 5) and time(index 6) are less than now
            event_datetime = event[5] + " " + event[6]
            self.assertTrue(event_datetime > datetime_now)


if __name__ == '__main__':
    unittest.main()
