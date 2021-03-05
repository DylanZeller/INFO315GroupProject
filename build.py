import sys
from src.automated_runner import AutomatedRunner

def get_options():
    return ''

def main(args):
    if len(args) <= 1:
        print('Please provide a build option. Your options are:')
        print(get_options())
        exit(1)
    if args[1] == 'test':
        ar = AutomatedRunner()
        ar.create_tables()

if __name__ == "__main__":
    main(sys.argv) 