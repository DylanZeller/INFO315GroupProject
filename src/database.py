from os import path
import sqlite3
from sqlite3 import Error
from .util import createLogger


class Database():
    db_file = ""
    conn = None
    log = createLogger(__name__)

    def __init__(self, database_file):
        self.db_file = path.abspath(database_file)
        self.connect()

    def connect(self):
        """ Try and connect to the database
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.log.info(f'Successfully connected to SQLite Database {self.db_file}')
        except Error as e:
            self.log.error(e)

    def create_table(self, create_table_cmd):
        """ Create a table from the create_table_cmd statement
        """
        self.execute_cmd(create_table_cmd)

    def insert(self, data_list, table):
        """ Insert row into table based on data_list
        """
        data_string = self.parse_data(data_list)
        insert_cmd = f'INSERT INTO {table} VALUES ({data_string});'
        self.execute_cmd(insert_cmd)
    
    def parse_data(self, data_list):
        """ Parse list of data into a string based on item types
        """
        l = []
        for item in data_list:
            if type(item) is str:
                l.append(f'\'{item}\'')
            else:
                l.append(item)
        return ','.join(l)

    def execute_cmd(self, cmd):
        """ Execute an SQL command
        """
        try:
            c = self.conn.cursor()
            c.execute(cmd)
            self.log.debug(f'Successfully executed command {cmd}')
        except Error as e:
            self.log.error(e)