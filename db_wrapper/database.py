from os import path
import re
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

    def select(self, table, params, conditions=None ):
        """ select rows from the parameters and optional conditions. 
        """
        param_string = ','.join(params)
        conditional_string = ''
        if conditions is not None :
            c = ' AND '.join(self.parse_data(conditions))
            conditional_string = f' WHERE ({c})'
        insert_cmd = f'SELECT {param_string} FROM {table}{conditional_string};'
        return self.execute_cmd(insert_cmd)

    def insert(self, table, data_list):
        """ Insert row into table based on data_list
        """
        data_string = ','.join(self.parse_data(data_list))
        insert_cmd = f'INSERT INTO {table} VALUES ({data_string});'
        self.execute_cmd(insert_cmd)

    def update(self, table, set_vals, conditions):
        """ Update statement constructed using sets and conditions 
            set_vals is a list of strings. ex) ['id = 12', 'f_name = \'John\'']
        """
        set_string = ','.join(self.parse_data(set_vals))
        conditional_string = ' AND '.join(self.parse_data(data_list))
        insert_cmd = f'UPDATE {table} SET {set_string} WHERE ({conditional_string});'
        self.execute_cmd(insert_cmd)

    def delete(self, table, conditions):
        """ Delete statement constructed using conditionals, where the conditions are strings 
        """
        conditional_string = ' AND '.join(self.parse_data(data_list))
        insert_cmd = f'DELTE FROM {table} WHERE ({conditional_string});'
        self.execute_cmd(insert_cmd)
    
    def parse_data(self, data_list):
        """ Parse list of data into a string based on item types
            returns a list of items based on the data list
        """
        l = []
        for item in data_list:
            if re.match(r'^-?\d+(?:\.\d+)$', item) is not None:
                l.append(item)
            else:
                l.append(f'\'{item}\'')
        return l

    def execute_cmd(self, cmd):
        """ Execute an SQL command
        """
        try:
            c = self.conn.cursor()
            c.execute(cmd)
            #self.log.debug(f'Successfully executed command {cmd}')
            return c.fetchall()
        except Error as e:
            self.log.debug(f'Error Executing command {cmd}')
            self.log.error(e)