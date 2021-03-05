from .database import Database
import .util

class AutomatedRunner():

    self.log = util.createLogger(__name__)

    def __init__(self, csv_file=None):
        self.csv_file = csv_file
        self.log.info(f'Created Automated Runner with csv_file={csv_file}')

    def run(self):
        pass
