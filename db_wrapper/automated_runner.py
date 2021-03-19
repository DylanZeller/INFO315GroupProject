from .database import Database
from .util import createLogger
from .constants import DEFAULT_DB_PATH
from .db_schema import ALL_TABLES, balance_trigger, bi_trigger_ne, bi_trigger
import csv

class AutomatedRunner():

    log = createLogger(__name__)

    def __init__(self, csv_file=None):
        self.csv_file = csv_file
        self.db = Database(DEFAULT_DB_PATH)
        self.log.info(f'Created Automated Runner with csv_file={csv_file}')

    def create_tables(self):
        for table_sql in ALL_TABLES:
            self.db.create_table(table_sql)

    def import_csv(self):
        with open(self.csv_file, 'r') as filestream:
            csv_reader = csv.reader(filestream, delimiter='|')
            for row in csv_reader:
                self.db.insert(row[0], row[1:])

    def add_triggers(self):
        self.db.execute_cmd(balance_trigger)
        self.log.info('Added Triggers Before')

    def add_triggers_after(self):
        self.db.execute_cmd(bi_trigger_ne)
        self.db.execute_cmd(bi_trigger)
        self.log.info('Added Triggers After')

    def get_commission_report(self):
        return self.db.get_commissions()

    def select_all(self, tableName):
        return self.db.select(tableName, '*')

    def select_attributes(self, tableName, attrs, conditions=None):
        """ select the certain attributes from the table name 
            attrs: list of attribute names to select
            conditions: list of conditions to be AND'd together
        """
        if conditions:
            return self.db.select(tableName, attrs, conditions)
        return self.db.select(tableName, attrs)
    
    def execute_custom_cmd(self, sql_cmd):
        return self.db.execute_cmd(sql_cmd)

    def test_trigger(self):
        args = ['67993546', '2', '1', '2', '2021-03-19', 'description', '100.00', 'Done']
        self.db.insert('billable_items', args)
        args = ['24929360', '12','76522729', '2', '2021-03-19', 'description', '100.00', 'Done']
        self.db.insert('billable_items', args)
        return self.select_all('invoice')

        
