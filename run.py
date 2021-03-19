import sys
from db_wrapper.automated_runner import AutomatedRunner
from os.path import abspath

def get_options():
    return ''

def main(args):
    if len(args) <= 1:
        print('Please provide a build option. Your options are:')
        print(get_options())
        exit(1)
    if args[1] == 'auto':
        ar = AutomatedRunner(abspath('./testData.csv'))
        ar.create_tables()
        ar.add_triggers()
        ar.import_csv()
        ar.add_triggers_after()
        print(ar.db.get_commissions()

if __name__ == "__main__":
    main(sys.argv) 