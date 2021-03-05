from .database import Database
from .util import createLogger
from .constants import DEFAULT_DB_PATH
from .db_schema import ALL_TABLES

class AutomatedRunner():

    log = createLogger(__name__)

    def __init__(self, csv_file=None):
        self.csv_file = csv_file
        self.db = Database(DEFAULT_DB_PATH)
        self.log.info(f'Created Automated Runner with csv_file={csv_file}')

    def create_tables(self):
        for table_sql in ALL_TABLES:
            self.db.create_table(table_sql)

    def run(self):
        pass