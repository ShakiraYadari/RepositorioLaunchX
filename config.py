from distutils.command.config import config
from msilib.schema import Error


def main():
    try:
        conguration = open('config.txt')
    except Exception:
        print("Couldn't find the config.txt file!")
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print('Found config.txt but it is a dictectory, could not read it' )
    except (BlockingIOError, TimeoutError):
        print("Cant complete raeding configuration bla bla")

if __name__ == '__main__':
    main()