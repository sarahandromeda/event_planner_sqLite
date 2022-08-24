import unittest
from unittest import TestCase
import os
from config import settings
from database.connection import Connection

"""
Tests components of connection.py file.
"""

class ConnectionTest(TestCase):
    def setUp(self):
        self.new_conn = Connection.create_connection('new.db')
        self.database_folder = os.path.join(
            settings.ROOT_DIR,
            settings.DB_FILE_LOCATION
        )

    def test_create_connection(self):
        self.assertIsNotNone(self.new_conn)

    def test_connection_location(self):
        file_list = os.listdir(self.database_folder)
        self.assertIn('new.db', file_list)
    
    def tearDown(self):
        os.remove(os.path.join(
            self.database_folder,
            'new.db'
        ))


if __name__ == '__main__':
    unittest.main()