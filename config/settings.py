import os

"""
All locations and names here a refered to via this file 
throughout the program allowing you to change these
settings before starting for the first time.

Settings may be changed after program has been initialized 
for the first time however, changing DEFAULT_CALENDAR_NAME
may introduce issues unless one or more of the other 
variables are also changed. 
"""

ROOT_DIR = os.getcwd()
DB_FILE_LOCATION = "calendars/"
DEFAULT_DB_FILE_NAME = 'planner.db'
DEFAULT_CALENDAR_NAME = 'my_calendar'
